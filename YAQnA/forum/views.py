from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from models import UserProfile, Question, Answer
from forms import UserForm, UserProfileForm, QuestionForm, AnswerForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    trending_question = Question.objects.all()[:5]
    return render(request,'forum/index.html',{'trending_question':trending_question,})


def about(request):
    return render(request,'forum/about.html',{})


def ask_question(request):
    if not request.user.is_authenticated():
        return render(request,'forum/login.html')
    question_form = QuestionForm()
    if request.method == "POST":
        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.user = request.user
            error_msg = None
            context_dict = {'question_form':question_form,'error_msg':error_msg}
            question.save()
            return HttpResponseRedirect('/forum/index')
        else:
            error_msg = question_form.errors
            return render(request,'forum/ask_question.html',{'error_msg':error_msg})
    else:
        return render(request,'forum/ask_question.html',{'question_form':question_form})

def question_detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'forum/question_detail.html',{'question':question})


def submit_answer(request, question_id):
    question = Question.objects.filter(pk=question_id)[0]
    if not request.user.is_authenticated():
        return render(request, 'forum/login.html')
    answer_form = AnswerForm()
    if request.method == "POST":
        answer_form = AnswerForm(data=request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.user = request.user
            answer.question = question
            error_msg = None
            answer.save()
            return HttpResponseRedirect('/forum/index')
        else:
            error_msg = answer_form.errors
            return render(request, 'forum/submit_answer.html', {'answer_form':answer_form,'question':question})
    else:
        return render(request, 'forum/submit_answer.html',{'answer_form':answer_form,'question':question})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/forum/index')
            else:
                return HttpResponse("Account Disabled")
        else:
            
                return HttpResponse("Invalid Login")
    else:
        return render(request,'forum/login.html',{})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/forum/')

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'forum/register.html',{'user_form':user_form, 'profile_form':profile_form,'registered':registered})




