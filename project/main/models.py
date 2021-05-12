from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
# Create your models here.
class User(AbstractUser):
    ... 

class Post(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    body = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
