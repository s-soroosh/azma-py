from django.conf.urls import patterns, url, include
from rest_framework import routers
from wage_meter import views

router = routers.DefaultRouter()
router.register(r'islands', views.IslandViewSet)


urlpatterns = patterns('',
                       # url(r'^(?i)$', views.get_islands, name='get_islands'),
                       # url(r'^(?i)islands$', views.get_islands, name='islands'),
                       # url(r'^(?i)techByIsland$', views.get_technology_by_island, name='tech_by_island'),
                       # url(r'^(?i)techByTech$', views.get_technology_by_parent_technology, name='tech_by_tech'),
                       url(r'^(?i)main$', views.main, name='main_view'),
                       url(r'^(?i)tech', views.tech, name='tech_view'),
                       url(r'tt/', include(router.urls)), )
