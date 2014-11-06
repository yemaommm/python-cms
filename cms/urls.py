from django.conf.urls import patterns, include, url
from django.contrib import admin
import os
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^files/',include('files.urls')),
    url(r'^cmsSQL/',include('cmsSQL.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'media/')}),

    url(r'', include('feincms.urls')),
    #url(r'^1',indx),
)
