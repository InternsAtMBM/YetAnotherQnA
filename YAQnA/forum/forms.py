from django import forms
from django.contrib.auth.models import User
from models import UserProfile, Question, Answer

class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=130,help_text="Please Provide Appropriate Title",required=True)
    text = forms.Textarea()
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0, required=False)
    follow = forms.IntegerField(widget=forms.HiddenInput(),initial=0, required=False)
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
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        super(forms.ModelForm, self).clean()
        if 'password' in self.cleaned_data and 'password_confirm' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
                self._errors['password'] = 'Password Should Match'
                self._errors['password_confirm'] = 'Passwords should match.'
        return self.cleaned_data
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)
