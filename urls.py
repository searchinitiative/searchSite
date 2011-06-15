from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from searchSite.views import IndexView,NewsView, ProfileSpecificView, ProfileView

from django.views.generic import *
from searchSite.articles.models import Article,Tag, CreateArticleForm
from searchSite.articles.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view()),
    url(r'^news$', NewsView.as_view()),

    url(r'^articles/(?P<pk>\d+)/$', DetailView.as_view(model = Article)),
    url(r'^articles/create/$','searchSite.articles.views.create'),
    url(r'^articles/newtag/$', CreateView.as_view(model = Tag)),
    url(r'^articles/tags/(?P<pk>\d+)$', 'searchSite.articles.views.tagview'),
    url(r'^articles/$',ListView.as_view(model = Tag)),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'accounts/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'template_name': 'accounts/logout.html'}),
    url(r'^accounts/register/$', 'searchSite.views.register'),
    url(r'^accounts/profile/$', ProfileView.as_view()),
    url(r'^accounts/profile/(?P<pk>\d+)$',ProfileSpecificView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
