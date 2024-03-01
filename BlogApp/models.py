from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Post.Status.PUBLISHED)

class Post(models.Model):


    title = models.CharField(max_length = 50, unique = True)
    content = models.TextField()
    category = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'post_images/ ')
    tags = ArrayField(models.CharField(max_length = 50))
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'published', 'Published'
        

    status = models.CharField(max_length = 20    , choices = Status.choices, default = Status.DRAFT)
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

        