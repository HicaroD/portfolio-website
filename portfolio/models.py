from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()

    class Meta():
        ordering = ['-posted']
