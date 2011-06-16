from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from searchSite.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view()),
    url(r'^news$', NewsView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('searchSite.accounts.urls')),
    url(r'^articles/', include('searchSite.articles.urls')),
    )



    # Uncomment the admin/doc line below to enable admin documentation:
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

