from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Article(models.Model):
    name = models.CharField(max_length=60)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
