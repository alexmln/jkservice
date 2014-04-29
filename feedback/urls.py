from django.conf.urls import patterns, url
from feedback import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^send_message/$', views.send_message, name='send_message'),
)
