from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from user_profile import views

__author__ = 'soroosh'

urlpatterns = patterns('',
                       url(r'^(?i)$', login_required(views.ProfileView.as_view()), name='show_profile'),
                       url(r'^(?i)/changepass$', views.change_password, name='change_password'),
                       )

