
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'houses.views.index', name='index'),
    url(r'^(?P<house_id>\d+)/$', 'houses.views.detail', name='detail'),
)