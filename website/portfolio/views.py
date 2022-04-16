from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Project

def index(request):
    return render(request, "portfolio/base.html")

def about_me(request):
    return render(request, "portfolio/about_me.html")

class Projects(ListView):
    model = Project
    template_name = "portfolio/projects.html"
