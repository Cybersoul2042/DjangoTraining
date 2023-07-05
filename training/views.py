from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("training:index"))
        else:
            return render(request, "training/index.html", {
                "form": form
            })
    return render(request, "training/index.html", {
        "form": NewTaskForm(),
        "tasks": request.session["tasks"]
    })
   
    