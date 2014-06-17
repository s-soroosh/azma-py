from django.conf.urls import patterns, url
from feincms.views.cbv.urls import handler

urlpatterns = patterns('',
                       # url(r'^(?i)$', views.index, name='home'),
                       # url(r'^(?i)what$', views.what, name='what'),
                       # url(r'^exam/(?i)(?P<exam_id>\d*)', views.intro, name='intro'),
                       # url(r'^start/(?i)(?P<exam_id>\d*)', views.start, name='start'),
                       # url(r'^$', include('feincms.urls'))),
                       url(r'^$', handler, name='feincms_home'),
                       url(r'^(.*)/$', handler, name='feincms_handler'),)


