from django.shortcuts import render, redirect
from django.http import Http404
from django import forms
from . import util
import random
import markdown2

from . import util


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    entry_content = util.get_entry(title)
    
    if entry_content is None:
        return render(request, "encyclopedia/error.html")
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown2.markdown(entry_content),
    })



def search(request):
    query = request.GET.get('q', '')
    entry = util.get_entry(query)
    entries = util.list_entries()
    if entry is not None:
        return redirect('entry', title=query)
    else:
        entries = util.list_entries()
        matches = [e for e in entries if query.lower() in e.lower()]
        if len(matches) == 0:
            return render(request, 'encyclopedia/no_results.html', {
                'query': query,
                "entries": entries,
                })
        else:
            return render(request, 'encyclopedia/search_results.html', {
                "matches": matches, 
                "query": query, 
            })



def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if util.get_entry(title) is None:
            util.save_entry(title, content)
            return redirect('entry', title=title)
        else:
            error = "Entry with this title already exists."
            return render(request, "encyclopedia/create.html", {"error": error})
    else:
        return render(request, "encyclopedia/create.html")



def edit(request, title):
    entry = util.get_entry(title)
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(title, content)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/edit.html", {"title": title, "content": entry})


def random_entry(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect('entry', title=random_entry)
