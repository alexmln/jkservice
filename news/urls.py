from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'news.views.index', name='index'),
)
