from django.conf.urls import patterns, url
from user import views

__author__ = 'soroosh'

urlpatterns = patterns('',
                       url(r'^(?i)login$', views.user_login, name='login'),
                       url(r'^(?i)logout$', views.user_logout, name='logout'),
                       url(r'^(?i)register$', views.user_register, name='register'),
                       url(r'^(?i)pending', views.show_pending, name='pending'),
                       url(r'^(?i)reconfirm', views.confirm_again, name='confirm_again'),
                       url(r'^(?i)confirm/(?P<user_id>\d*)-(?P<confirm_code>\w*)$', views.confirm, name='confirm'),
)
