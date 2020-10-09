from django.shortcuts import render

from . import util
from markdown2 import Markdown
from django import forms


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()

    })

def entry(request,title):
    entries= util.list_entries()
    if title in entries:
        entrypage= util.get_entry(title)
        convertpage= Markdown().convert(entrypage)

        content={
            'entrypage':convertpage,
            'title': title,
        }

        return render(request, "encyclopedia/entries.html",content)
    else:
        return render(request, "encyclopedia/error.html")

class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass', 'placeholder': 'Search'}))

class Post(forms.Form):
    title = forms.CharField(label= "Title")
    textarea = forms.CharField(widget=forms.Textarea(), label='')

class Edit(forms.Form):
    textarea = forms.CharField(widget=forms.Textarea(), label='')


def edit(request,title):
    if request.method == 'GET':
        editpage= util.get_entry(title)

        content={
            'editform': Search(),
            'edit': Edit(initial= {'textarea':editpage}),
            'title': title
        }
        return render(request,"encyclopedia/edit.html", content)
    else:
        form = Edit(request.POST) 
        if form.is_valid():
            textarea = form.cleaned_data["textarea"]
            util.save_entry(title,textarea)
            editpage = util.get_entry(title)
            page_converted = Markdown().convert(editpage)

            content = {
                'editform': Search(),
                'editpage': page_converted,
                'title': title
            }
            return render(request, "encyclopedia/entries.html", content)


    
    

