from django.shortcuts import render
from .models import BlogPost

# Create your views here.

def blog(request):
    bps = BlogPost.objects.all()
    return render(request, "myapp/blog.html", {"blogs": bps})
