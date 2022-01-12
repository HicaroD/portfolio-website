from django.urls import path

from . import views

urlpatterns = [
        path('', views.home, name = "index"),
        path('about_me/', views.about_me, name = "about_me"),
        path('contact/', views.contact, name = "contact"),
        path('article/<slug:slug>', views.article, name = "article")
]
