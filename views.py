from django.views.generic import TemplateView

from searchSite.annoying.decorators import render_to

class IndexView(TemplateView):
   template_name= "index.html"

class NewsView(TemplateView):
   template_name= "news.html"


