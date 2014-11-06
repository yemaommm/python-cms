from django.conf.urls import patterns, include, url
from cmsSQL.views import *
import os


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^posttable',posttable),
    url(r'^postdb',postdb),
    url(r'^postConn',postConn),
    url(r'^',dbQ),
)
