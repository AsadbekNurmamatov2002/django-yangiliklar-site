from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class PostName(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    image=models.ImageField(default='')
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=250, unique=True)
    body=RichTextUploadingField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField( auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    auther=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    postname=models.ForeignKey(PostName, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-publish']
    def get_absolute_url(self):
        return reverse('myapp:postditile', args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug])

class Message(models.Model):
    Mbody=models.TextField()
    auther=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post=models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    created=models.DateTimeField( auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Mbody[0:30]
    