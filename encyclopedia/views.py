from django.shortcuts import render

from . import util
from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html",{
        "entries": util.list_entries()
    })

def entry(request,title):
    myentries= util.list_entries()

    for title in myentries:
        entrypage = util.get_entry(title)
        pageconverted= Markdown().convert(entrypage)
    
        content={
            'page':entrypage,
            'title':title
        }
    return render(request, "encyclopedia/entries.html",content)


def create(request):
    return render(request, "encyclopedia/create.html")

def randomm(request):
    return render(request, "encyclopedia/random.html")