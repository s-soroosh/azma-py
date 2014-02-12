from django.conf.urls import patterns, url
from user_profile import views

__author__ = 'soroosh'

urlpatterns = patterns('',
                       url(r'^(?i)$', views.show_profile, name='show_profile'))

