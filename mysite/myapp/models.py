from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    date_created = models.DateTimeField(verbose_name="Date created", auto_now_add=True)
    text = models.TextField()
