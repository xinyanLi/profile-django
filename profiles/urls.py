from django.conf.urls import patterns, url, include
from profiles import views
from .views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/profiles/$', ProfileList.as_view(), name='profile-list'),
    url(r'^api/profiles/(?P<pk>[0-9]+)$', ProfileDetail.as_view() , name='profile-detail'),
]



