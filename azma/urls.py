from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from azma import views


admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'azma.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^blog/', include('elephantblog.urls')),
                       url(r'^weblog/', include('zinnia.urls')),
                       url(r'^comments/', include('django.contrib.comments.urls')),
                       url(r'^(?i)admin/', include(admin.site.urls)),
                       url(r'^(?i)about', views.about, name='about'),
                       url(r'^(?i)user/', include('user.urls')),
                       url(r'^(?i)profile', include('user_profile.urls', namespace='profile')),
                       url(r'^(?i)wage_meter/', include('wage_meter.urls', namespace='wages')),
                       url(r'^(?i)answer/', include('answer.urls', namespace='answer')),
                       url(r'^', include('exam.urls', namespace='exam')),
)

urlpatterns += staticfiles_urlpatterns()



