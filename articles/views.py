from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Template
from django.views.generic import DetailView, ListView

from django.contrib.auth.decorators import login_required

from searchSite.articles.models import CreateArticleForm

from django.shortcuts import render_to_response, get_object_or_404
from searchSite.articles.models import Article, Tag

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


def tagView(request,pk):
   template_name = "articles/tagview.html"
   tag = get_object_or_404(Tag, pk=pk)
   articles = tag.article_set.all()
   return render_to_response('articles/tagView.html', {'tag':tag, 'articles':articles}, context_instance=RequestContext(request))

def articleView(request,pk):
   template_name = "articles/articleview.html"
   article = get_object_or_404(Article, pk=pk)
   comments = article.comment_set.all()
   return render_to_response('articles/articleView.html', {'article':article, 'comments':comments}, context_instance=RequestContext(request))

def getTagList(request):
   return {'top5tags': Tag.objects.all()[:5]}
