from django.conf.urls import patterns, url
from wage_meter import views



urlpatterns = patterns('',
                       url(r'^(?i)$', views.get_islands, name='get_islands'),
                       url(r'^(?i)islands$', views.get_islands, name='islands'),
                       url(r'^(?i)techByIsland$', views.get_technology_by_island, name='tech_by_island'),
                       url(r'^(?i)techByTech$', views.get_technology_by_parent_technology, name='tech_by_tech'),
)
