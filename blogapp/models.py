from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField

fs = FileSystemStorage(location='/tmp')
blogimage = FileSystemStorage(location='/tmp')


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField()
    description = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = models.FileField(default=None, null=True, storage=blogimage)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
