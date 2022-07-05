from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Dialogue(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.text


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    likes = models.IntegerField()
    pud_date = models.DateTimeField(default=timezone.now())


class Comment(models.Model):
    content = models.TextField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)


class Image(models.Model):
    image = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image', null=True)
    