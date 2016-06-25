from django.conf.urls import url
from forum import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$', views.user_logout,name='user_logout'),
]
