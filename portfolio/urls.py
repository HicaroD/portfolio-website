from django.urls import path

from . import views

urlpatterns = [
        path('', views.about_me, name = "about_me"),
        path('projects/', views.Projects.as_view(), name = "projects")
]
