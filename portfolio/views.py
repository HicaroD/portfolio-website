from django.shortcuts import render, HttpResponse, get_object_or_404
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

def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "portfolio/article.html", {'article':article})
