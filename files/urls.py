from django.conf.urls import patterns, include, url
from files.views import *
import os


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^one/', one),
    url(r'^',index),
)
