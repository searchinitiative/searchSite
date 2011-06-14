from django.http import HttpResponse
from django.views.generic import DetailView


def detail(response,ident):
   return HttpResponse('Hello peeps' + ident)

