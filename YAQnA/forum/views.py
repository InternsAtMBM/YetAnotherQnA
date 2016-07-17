from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, Question, Answer, User
from .forms import UserForm, UserProfileForm, QuestionForm, AnswerForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    trending_question = Question.objects.order_by('-views')[:5]
    return render(request, 'forum/index.html', {'trending_question':trending_question, })


def about(request):
    return render(request, 'forum/about.html',{})


def ask_question(request):
    #error_msg = "outside POST"
    if not request.user.is_authenticated():
        return render(request,'forum/login.html')
    question_form = QuestionForm()
    if request.method == "POST":
        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.user = request.user
            #error_msg = "inside post"
            question.save()
            return HttpResponseRedirect('/forum/index')
        else:
            error_msg = question_form.errors
            return render(request,'forum/ask_question.html',{'question_form':question_form})
    else:
        return render(request,'forum/ask_question.html',{'question_form':question_form})

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.views = question.views + 1
    question.save()
    answer_set = Answer.objects.filter(question=question)
    question_vote = question.rating.get_rating_for_user(request.user, request.META['REMOTE_ADDR'])
    answer_mega_set = []
    for answer in answer_set:
        answer_mega_set.append({'username': answer.user.username,'id':answer.id,'rating_likes':answer.rating_likes,
                                'rating_dislikes':answer.rating_dislikes,'text':answer.text,
                                "chk_user_vote": answer.rating.get_rating_for_user(request.user, request.META['REMOTE_ADDR'])
                                })

    print answer_mega_set
    context = {'question':question, 'answer_set': answer_set, 'question_vote': question_vote
               ,'answer_mega_set': answer_mega_set}

    return render(request, 'forum/question_detail.html', context)

def submit_answer(request, question_id):
    question = Question.objects.filter(pk=question_id)[0]
    if not request.user.is_authenticated():
        return render(request, 'forum/login.html')
    chk_duplicate = Answer.objects.filter(user=request.user, question=question)
    if chk_duplicate:
        return HttpResponse("You Can not answer more than one time for a particular Question")

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
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'forum/register.html',{'user_form':user_form, 'profile_form':profile_form,'registered':registered})

def show_profile(request,username):
    USER = get_object_or_404(User,username=username)
    user_profile = get_object_or_404(UserProfile,user=USER)
    return render(request,'forum/show_profile.html',{'USER':USER,'user_profile':user_profile})

def list_domains(request):
    domains = Question.objects.order_by().values_list('domain').distinct()
    domain_info = {}
    for domain in domains:
        domain_info[domain[0]]= Question.objects.filter(domain=domain[0]).count()

    for key in domain_info.keys():
        print key,domain_info[key]
    return render(request,'forum/list_domains.html', {'domain_info':domain_info})

def show_domain(request,domain):
    questions = Question.objects.filter(domain=domain)
    return render(request,'forum/show_domain.html', {'questions': questions})

