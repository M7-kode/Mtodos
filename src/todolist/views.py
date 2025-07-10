from django.shortcuts import render, redirect
from .models import NoteModel
from datetime import datetime
# Create your views here.

def index(request):
    note = NoteModel.objects.all()
    return render(request, "index.html", context={
        "note": note,
    })

def add_page(request):
    return render(request, "add.html")

def add_note(request):
    titre_name = request.POST.get("titre")
    description_name = request.POST.get("description")
    date_data = datetime.now()
    NoteModel.objects.create(titre = titre_name,description = description_name, date=date_data)
    return redirect("index-page")

def note_details(request, slug):
    note = NoteModel.objects.get(slug=slug)
    return render(request, "note_details.html", context={
        "note": note,
    })

def update_page(request,slug):
    note =  NoteModel.objects.get(slug=slug)
    return render(request, "update_page.html", context={
        "note":note,
    })

def update_note(request,slug):
    titre_name = request.POST.get("titre")
    description_name = request.POST.get("description")
    date_data = datetime.now()
    b = NoteModel.objects.get(slug=slug)
    b.titre = titre_name
    b.description = description_name
    b.date = date_data
    b.save()
    return redirect("index-page")

def delete_page(request, pk):
    note = NoteModel.objects.get(pk=pk)
    return render(request, "delete_page.html", context={
        "note": note,
    })
def delete_note(request,pk):
    if request.POST.get("oui"):
        note = NoteModel.objects.get(pk=pk)
        note.delete()
    else:
        pass
    return redirect("index-page")