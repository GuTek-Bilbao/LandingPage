from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

LANG = (
    ('ES', "Español"),
    ('EN', "English"),
    ('EU', "Euskara")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="uploads/", verbose_name="image")
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='blog_posts_author')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='blog_post_content')
    lang = models.CharField(choices=LANG, max_length=2)
    content = models.TextField()
    translator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="blog_post_translator")
