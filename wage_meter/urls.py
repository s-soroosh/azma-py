from django.conf.urls import patterns, url
from wage_meter import views



urlpatterns = patterns('',
                       url(r'^(?i)$', views.get_islands, name='get_islands'))