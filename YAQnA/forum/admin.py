from django.contrib import admin
from models import UserProfile, Question, Answer, Vote
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Vote)
