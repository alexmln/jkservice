from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'jkservice.views.index', name='index'),
    url(r'^whiteroom/', include(admin.site.urls)),
    url(r'^watermet/', 'jkservice.views.watermet', name='watermet'),
    url(r'^add_statement/', 'jkservice.views.add_statement', name='add_statement'),
    url(r'^captacha/', include('captcha.urls')),
    url(r'^captcha_refresh/', 'jkservice.views.captcha_refresh', name='captcha_refresh'),
    url(r'^houses/', include('houses.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^feedback/', include('feedback.urls')),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))