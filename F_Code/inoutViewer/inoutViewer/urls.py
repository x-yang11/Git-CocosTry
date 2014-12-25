from django.conf.urls import patterns, include, url
from django.contrib import admin
from inoutViewer.view import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inoutViewer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', inoutviewer_hello),
    url(r'^time/$', inoutviewer_time),
    url(r'^time/plus/(\d{1,3})/$', inoutviewer_time_offset),
    url(r'^thanks/$', inout_template),
)
