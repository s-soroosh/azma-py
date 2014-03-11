__author__ = 'SOROOSH'

from django.conf.urls import patterns, url
from answer import views

urlpatterns = patterns('',
                       url(r'^analyze/(?i)(?P<exam_id>\d*)', views.analyze_answer, name='analyze'),
)


