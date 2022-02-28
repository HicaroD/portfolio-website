from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView 
from django.views.generic.list import ListView

from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"
    context_object_name  = "articles"

class ArticleDetailView(DetailView):
    model = Article
