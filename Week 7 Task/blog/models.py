from django.db import models
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(unique = True, max_lenght = 200)
    body = models.TextField()

    def __str__(self):
        return self.title
    