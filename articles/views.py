from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required

from searchSite.articles.models import CreateArticleForm, CreateCommentForm

from django.shortcuts import get_object_or_404
from searchSite.articles.models import Article, Tag, Comment

from searchSite.annoying.decorators import render_to

@render_to('articles/create.html')
@login_required
def create(request):

   if request.method == 'POST':
      b = Article( author = request.user)
      form = CreateArticleForm(request.POST, instance = b)
      if form.is_valid():
         b.save()
         return HttpResponseRedirect('/articles/%d' % b.pk)

   else:
      form = CreateArticleForm()

   return {'form':form}


@render_to('articles/tagView.html')
def tagView(request,pk):
   tag = get_object_or_404(Tag, pk=pk)
   articles = tag.article_set.all()
   return  {'tag':tag, 'articles':articles}

@render_to('articles/articleView.html')
def articleView(request,pk):

   article = get_object_or_404(Article, pk=pk)
   comments = article.comment_set.all()

   if (request.method == 'POST' and request.user.is_authenticated()):
      c = Comment(article = article)
      form = CreateCommentForm(request.POST,instance = c)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('')

   else:
      form = CreateCommentForm()

   return  {'article':article, 'comments':comments, 'form':form}

def getTagList(request):
   return {'top5tags': Tag.objects.all()[:5]}

import json

def submitComment(request,pk):
   b = json.dumps({'error':True})

   if (request.method == 'POST' and request.user.is_authenticated()):
      article = get_object_or_404(Article,pk = pk)
      f = Comment(article = article)
      form = CreateCommentForm(request.POST,instance = f)
      if form.is_valid():
         c = form.save()
         b = json.dumps({'comment':c.text, 'error':False})

   return HttpResponse(b,mimetype='application/json')
