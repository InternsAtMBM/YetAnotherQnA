from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Permission, User
'''
class Question(models.Model):
    asker = models.ForeignKey(User)
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=1000)

class Answer(models.Model)
    question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=1000)
'''
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    profile_picture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return self.user.username
