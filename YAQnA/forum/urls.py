from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$', views.user_logout,name='user_logout'),
    url(r'^ask_question/$', views.ask_question, name='ask_question'),
    url(r'^submit_answer/(?P<question_id>[0-9]+)/$', views.submit_answer, name='submit_answer'),
    url(r'^question_detail/(?P<question_id>[0-9]+)/$', views.question_detail, name='question_detail'),
    url(r'^(?P<username>\w+)/$', views.show_profile, name='show_profile'),
]
