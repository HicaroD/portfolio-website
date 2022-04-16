from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from articles.models import Article

class ArticleListView(ListView):
    model = Article
    template_name = "articles/homepage.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_page.html"
