from django.db import models

# Create your models here.

class model(models.Model):
    content = models.TextField()
    created_time  = models.DateField(auto_now_add = True)
    modified_time = models.DateField(auto_now = True)

    def __str__(self):
        return self.content
