from django.conf.urls import patterns, include, url
from django.contrib import admin
from view import inoutviewer

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inoutViewer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^inoutviewer/', inoutviewer),
)
