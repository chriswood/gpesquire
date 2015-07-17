from django.conf.urls import patterns, include, url
from django.contrib import admin
from gpesq.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gpesquire.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'index'),
    url(r'^add_point/$', add_point),
    #url(r'^admin/', include(admin.site.urls)),
)
