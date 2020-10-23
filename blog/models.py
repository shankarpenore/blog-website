from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date_posted = models.DateField(verbose_name='created on', auto_now_add=True)
    content = models.TextField(max_length=512)
    likedby = models.ManyToManyField(User,related_name='likes',blank=True)
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/display_posts/{self.id}'

    def get_total_likes(self):
        return self.likedby.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # post = models.ManyToManyField(Post,related_name='comments')
    comment = models.CharField(max_length=255)
    commenter = models.ForeignKey(User,on_delete=models.CASCADE)
    date_commented = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.comment)

    def __unicode__(self):
        return str(self.comment)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

