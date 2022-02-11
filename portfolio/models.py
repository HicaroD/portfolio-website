from django.db import models
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    technologies = models.TextField(null=True)   # List of technologies separated by comma
    project_link = models.CharField(max_length=100, null=True)
    rating = models.SmallIntegerField() # For ordering

    def __str__(self):
        return self.title

    def get_technologies(self):
        return self.technologies.split(",")

    class Meta():
        ordering = ['-rating']
