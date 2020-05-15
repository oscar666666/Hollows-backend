from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  
# Create your models here.
class Communities(models.Model):
    Community_Name = models.CharField(max_length=64)
    CreateDate = models.DateTimeField(default=datetime.now)

class Thread(models.Model):

    Title = models.CharField(max_length=64)
    body = models.TextField()
    Post_time = models.DateTimeField(default=datetime.now)
    SoftDelete = models.BooleanField(default=False)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):

    Body = models.TextField()
    Post_time = models.DateTimeField(default=datetime.now)
    SoftDelete = models.BooleanField(default=False)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    T_id = models.ForeignKey(Thread, on_delete=models.CASCADE, default=1)

class Reply(models.Model):

    Body = models.TextField()
    Post_time = models.DateTimeField(default=datetime.now)
    SoftDelete = models.BooleanField(default=False)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    P_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class Subscribtion(models.Model):
    c_id = models.ForeignKey(Communities, on_delete=models.CASCADE)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Upvote(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    P_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class GoodReply(models.Model):
    T_id = models.ForeignKey(Thread, on_delete=models.CASCADE)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    P_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class Watch(models.Model):
    T_id = models.ForeignKey(Thread, on_delete=models.CASCADE)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)