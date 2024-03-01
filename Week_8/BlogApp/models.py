from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Post(models.Model):


    title = models.CharField(max_length = 25,unique = True)
    content = models.TextField()
    category = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'post_images/ ')
    tags = ArrayField(models.CharField(max_length = 50))

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'published', 'Published'
        

    status = models.CharField(max_length = 20, choice = Status.choices, default = Status.DRAFT)
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

        # app_label = 'BlogApp'