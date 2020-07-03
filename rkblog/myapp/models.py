from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.

class CustomManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='publish')

class Post(models.Model):
    STATUS_CHOICE=(('draft','Draft'),('publish','Published'))
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=260,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='block_post',on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=15,choices=STATUS_CHOICE,default='draft')
    objects=CustomManager()
    tags=TaggableManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail",args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
    

class CustomManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().order_by('-created')

class comment(models.Model):
    post=models.ForeignKey(Post,related_name='comment',on_delete=Post)
    name=models.CharField(max_length=120)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    objects=CustomManager()
    
    def __str__(self):
        return 'created by {} on {}'.format(self.name,self.post)
    