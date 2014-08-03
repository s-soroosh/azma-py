from tutorial.views import *
from tutorial import views

__author__ = 'SOROOSH'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', TutorialView.as_view(), name="home"),
                       url(r'^cat/(?P<category_name>.*)$', TutorialWithCategoryView.as_view(), name="category"),
                       url(r'^tutorial_analyze/(?P<exam_tu_id>.*)', TutorialAnswerAnalyze.as_view(), name='tutorial_exam_analyze'),
                       url(r'^tutorial_exam/(?P<tutorial_id>.*)', TutorialExamView.as_view(), name='tutorial_exam'),
                       url(r'^(?P<tutorial_name>.*)$', TutorialDetailView.as_view(), name="tutorial"),




)

