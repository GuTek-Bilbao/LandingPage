from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# BUG: models are not migrated to the database for some reason

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

LANG = (
    ('es', "Español"),
    ('en', "English"),
    ('eu', "Euskara")
)


class Post(models.Model):
    original_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="uploads", verbose_name="image", width_field=625, height_field=320) # TODO add width and height 
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='blog_posts_author')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']


class PostContent(models.Model):
    title =models.CharField(max_length=200, unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='blog_post_content')
    lang = models.CharField(choices=LANG, max_length=2)
    content = models.TextField()
    translator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="blog_post_translator")

    def __str__(self):
        return self.title