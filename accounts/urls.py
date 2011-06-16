from django.conf.urls.defaults import patterns, include, url

from django.views.generic import *

from django.contrib.auth.decorators import login_required
from searchSite.accounts.views import *

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'accounts/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'template_name': 'accounts/logout.html'}),
    url(r'^register/$', 'searchSite.accounts.views.register'),
    url(r'^profile/$', login_required(ProfileView.as_view())),
    url(r'^profile/(?P<pk>\d+)$',ProfileSpecificView.as_view()))
