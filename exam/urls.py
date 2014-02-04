from django.conf.urls import patterns, url
from exam import views

urlpatterns = patterns('',
                       url(r'^(?i)$', views.index, name='home')
)