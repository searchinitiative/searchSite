from django.conf.urls.defaults import patterns, include, url

from searchSite.articles.views import *

from django.views.generic import *
from searchSite.articles.models import Article,Tag

from django.contrib.auth.decorators import login_required

urlpatterns = patterns('searchSite.articles.views',
    url(r'^(?P<pk>\d+)/$', 'articleView'),
    url(r'^create/$','create'),
    url(r'^newtag/$', login_required(CreateView.as_view(model = Tag))),
    url(r'^tags/(?P<pk>\d+)$', 'tagView'),
    url(r'^$',ListView.as_view(model = Tag)))