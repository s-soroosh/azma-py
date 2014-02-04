from django.conf.urls import patterns, url
from user import views

__author__ = 'soroosh'

urlpatterns = patterns('',
                       url(r'^login$', views.user_login, name='login'),
                       url(r'^logout$', views.user_logout, name='logout'),
                       url(r'^register$', views.user_register, name='register'),
                       url(r'^pending', views.show_pending, name='pending'),
                       url(r'^pending', views.show_pending, name='confirm_again'),
                       )
