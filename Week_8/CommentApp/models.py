from django.db import models
from BlogApp.models import Post
# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    author = models.CharField()
    published_date = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.Author}: {self.Content}"
    
    class Meta:
        app_label = 'CommentApp'