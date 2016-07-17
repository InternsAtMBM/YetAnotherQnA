from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Permission, User
from updown.fields import RatingField

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to='profile_images', blank=True, null=True, default="profile_images/default.jpg")
    website = models.URLField(blank=True)
    about = models.TextField(blank=True)
    def __unicode__(self):
        return self.user.username



class Question(models.Model):
    domain = models.CharField(max_length=30,blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300,blank=False)
    text = models.CharField(max_length=1000,blank=True)
    views = models.IntegerField(default=0)
    rating = RatingField(can_change_vote=True)

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000,blank=False)
    rating = RatingField(can_change_vote=True)

    def __unicode__(self):
        return self.text+" ->"+self.user.username


