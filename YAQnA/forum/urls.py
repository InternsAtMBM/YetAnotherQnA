from django.conf.urls import url
from . import views
from updown.views import AddRatingFromModel
app_name = 'forum'
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
    url(r'^question/(?P<object_id>[0-9]+)/rate/(?P<score>[\d\-]+)/$', AddRatingFromModel(), {
    'app_label': 'forum',
    'model': 'Question',
    'field_name': 'rating',
    }, name="question_rating",),

    url(r'^answer/(?P<object_id>[0-9]+)/rate/(?P<score>[\d\-]+)/$', AddRatingFromModel(), {
        'app_label': 'forum',
        'model': 'Answer',
        'field_name': 'rating',
    }, name="answer_rating"),

    url(r'^domains/$', views.list_domains, name='list_domains'),
    url(r'^domains/(?P<domain>\w+)/$', views.show_domain, name='show_domain'),
    url(r'^user/(?P<username>\w+)/$', views.show_profile, name='show_profile'),


]
