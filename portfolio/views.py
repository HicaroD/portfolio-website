from django.shortcuts import render, HttpResponse
from .models import Article

def index(request):
    return render(request, "portfolio/base.html")

def home(request):
    articles = Article.objects.all()
    return render(request, "portfolio/home.html", {'articles':articles})

def about_me(request):
    return render(request, "portfolio/about_me.html")

def contact(request):
    return render(request, "portfolio/contact.html")
