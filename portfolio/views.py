from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article

def index(request):
    return render(request, "portfolio/base.html")

def about_me(request):
    return render(request, "portfolio/about_me.html")

def contact(request):
    return render(request, "portfolio/contact.html")
