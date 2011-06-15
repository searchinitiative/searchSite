from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Template
from django.views.generic import DetailView

from django.contrib.auth.decorators import login_required

from articles.models import CreateArticleForm

from django.shortcuts import render_to_response
from articles.models import Article

@login_required
def create(request):

   if request.method == 'POST':
      form = CreateArticleForm(request.POST)
      if form.is_valid():
         formName = form.cleaned_data['name']
         formTag = form.cleaned_data['tag']
         formText = form.cleaned_data['text']
         b = Article(name = formName, tag = formTag, author = request.user, text = formText)
         b.save()
         return HttpResponseRedirect('/articles/%d' % b.pk)

   else:
      form = CreateArticleForm()

   return render_to_response('articles/create.html', {'form':form}, context_instance=RequestContext(request))


def detail(response,ident):
   return HttpResponse('Hello peeps' + ident)

