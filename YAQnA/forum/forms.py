from django import forms
from django.contrib.auth.models import User
from models import UserProfile, Question, Answer
import re

class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=130,help_text="Please Provide Appropriate Title",required=True)
    text = forms.CharField(widget=forms.Textarea)
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0, required=False)
    follow = forms.IntegerField(widget=forms.HiddenInput(),initial=0, required=False)
    domain = forms.CharField(max_length=40,required=True)
    
    
    class Meta:
        model = Question
        fields = ('domain','title', 'text',)


class AnswerForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    upvotes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    downvotes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    
    
    class Meta:
        model = Answer
        fields = ('text',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    password_confirm = forms.CharField(widget=forms.PasswordInput(),required=True)
    email = forms.EmailField(required=True)

    def password_score(self):
        count = 0
        password = self.cleaned_data['password']
        if len(password) >= 6:
            count += 10
        if re.search(r'[A-Z]+', password):
            count += 10
        if re.search(r'[a-z]+', password):
            count += 10
        if re.search(r'[0-9]+', password):
            count += 10
        if re.search(r'!@#$%', password):
            count += 10
        return count

    def clean(self):
        super(forms.ModelForm, self).clean()
        if 'email' in self.cleaned_data:
            email = self.cleaned_data['email']
            username = self.cleaned_data['username']
            if email and User.objects.filter(email=email).exclude(username=username).count() > 0:
                print email, username,"ok gotch"
                self._errors['email']='Email Already Taken'
                raise forms.ValidationError("This Email Address is already taken")
        else:
            print "why why why" * 10
            raise forms.ValidationError("Must Provide Email Address")

        if 'password' in self.cleaned_data and 'password_confirm' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
                self._errors['password'] = 'Password Should Match'
                self._errors['password_confirm'] = 'Passwords should match.'
            elif self.password_score() < 40:
                self._errors['password'] = 'Password Length must be atleast 6 and must have atleast one Uppercase,Lowercase and Digit'
                self._errors['password_confirmm'] = 'Password Length must be atleast 6 and must have atleast one Uppercase,Lowercase and Digit'
        else:
            raise forms.ValidationError("Password Can not be Blank")



        return self.cleaned_data
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('profile_picture', 'website', 'about')
