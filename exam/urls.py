from django.conf.urls import patterns, url
from exam import views

urlpatterns = patterns('',
                       url(r'^(?i)$', views.index, name='home'),
                       url(r'^(?i)what$', views.what, name='what'),
                       url(r'^exam/(?i)(?P<exam_id>\d*)', views.intro, name='intro'),
                       url(r'^start/(?i)(?P<exam_id>\d*)', views.start, name='start'),
                       url(r'^(?i)cat/(?P<category_id>\d*)', views.sub_categories, name='sub_categories')
)

