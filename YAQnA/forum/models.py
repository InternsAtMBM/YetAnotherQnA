from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Permission, User


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
    rating  =
    def __unicode__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000,blank=False)

    def __unicode__(self):
        return self.text+" ->"+self.user.username

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question_vote = models.IntegerField(default=0)
    answer_vote = models.IntegerField(default=0)

    def __unicode__(self):
        return  self.user.username + " q_vote:"+str(self.question_vote) +  " a_vote:"+str(self.answer_vote)
