from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=50)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    slug = models.SlugField(max_length=50, null=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={'slug': self.slug})

    class Meta():
        ordering = ['-posted']
