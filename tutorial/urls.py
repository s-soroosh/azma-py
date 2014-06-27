from tutorial.views import TutorialView

__author__ = 'SOROOSH'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', TutorialView.as_view(), name="home")
)

