from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    return render(request, "index.html")


def blog(request):
    posts = models.PostContent.objects.filter(lang=request.LANGUAGE_CODE, post__status=1)
    return render(request, "blog.html", {'posts':posts})

def post_view(request, slug):
    content = models.PostContent.objects.filter(post__slug=slug, lang=request.LANGUAGE_CODE)
    return render(request, "post.html", {'content' : content})