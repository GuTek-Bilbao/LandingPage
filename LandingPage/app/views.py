from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    return render(request, "index.html")


def blog(request):
    posts = models.Post.objects.order_by('created_on')
    contents = models.PostContent.objects.filter(lang=request.LANGUAGE_CODE)
    return render(request, "blog.html", {'contents' : contents, 'posts':posts})

def post_view(request, slug):
    content = models.PostContent.objects.filter(post__slug=slug, lang=request.LANGUAGE_CODE)
    return render(request, "post.html", {'content' : content})