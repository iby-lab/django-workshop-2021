from django.contrib import admin
from .models import BlogPost

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    fields = ["title", "author", "text"]

admin.site.register(BlogPost, BlogPostAdmin)
