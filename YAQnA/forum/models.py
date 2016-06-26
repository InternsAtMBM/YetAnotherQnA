from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Permission, User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


class Question(models.Model):
    domain = models.CharField(max_length=30,blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300,blank=False)
    text = models.CharField(max_length=1000)
    views = models.IntegerField(default=0)
    follow = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000,blank=False)

    def __unicode__(self):
        return self.text+" ->"+self.user.username