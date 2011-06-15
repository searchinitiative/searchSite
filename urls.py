from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from searchSite.views import IndexView

from django.views.generic import DetailView
from searchSite.articles.models import Article

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view()),
    url(r'^articles/(?P<pk>\d+)/$', DetailView.as_view(model = Article)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'accounts/login.html'}),
    url(r'^accounts/register/$', 'searchSite.views.register'),

    # Uncomment the admin/doc line below to enable admin documentation:
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
