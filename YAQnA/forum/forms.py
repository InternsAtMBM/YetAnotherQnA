from django import forms
from django.contrib.auth.models import User
from models import UserProfile, Question, Answer

class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=130,help_text="Please Provide Appropriate Title",required=True)
    text = forms.Textarea()
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    follow = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    domain = forms.CharField(max_length=40,required=True)
    class Meta:
        model = Question
        fields = ('domain','title', 'text',)


class AnswerForm(forms.ModelForm):
    text = forms.Textarea()
    upvotes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    downvotes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)

    class Meta:
        model = Answer
        fields = ('text',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput()) 
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)
