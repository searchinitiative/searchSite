from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required

from searchSite.articles.models import CreateArticleForm, CreateCommentForm, EditArticleForm, EditCommentForm

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
   for comment in comments:
      if comment.author == request.user:
         comment.canEdit = True
         comment.editForm = EditCommentForm(instance = comment)

   if (request.method == 'POST' and request.user.is_authenticated()):
      c = Comment(article = article, author=request.user)
      form = CreateCommentForm(request.POST,instance = c)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('')

   else:
      form = CreateCommentForm()

   editForm = EditArticleForm(instance = article)
   canEdit = (request.user == article.author)

   return  {'article':article, 'comments':comments, 'form':form, 'editForm':editForm, 'canEdit':canEdit}

def getTagList(request):
   return {'top5tags': Tag.objects.all()[:5]}


@render_to('articles/editArticleView.html')
def editArticleView(request,pk):

   article = get_object_or_404(Article, pk=pk,author = request.user)

   if (request.method == 'POST' and request.user.is_authenticated()):
      form = EditArticleForm(request.POST, instance = article)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/articles/' + str(article.id) + '/')

   else:
      form = EditArticleForm(instance = article )


   return  {'article':article, 'form':form }

@render_to('articles/editCommentView.html')
def editCommentView(request,pk):

   comment = get_object_or_404(Comment, pk=pk,author = request.user)

   if (request.method == 'POST' and request.user.is_authenticated()):
      form = EditCommentForm(request.POST, instance = comment)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/articles/' + str(comment.article.id) + '/')

   else:
      form = EditCommentForm(instance = comment )


   return  {'comment':comment, 'form':form }


import json

def submitComment(request,pk):
   b = json.dumps({'error':True})

   if (request.method == 'POST' and request.user.is_authenticated()):
      article = get_object_or_404(Article,pk = pk)
      f = Comment(article = article, author=request.user)
      form = CreateCommentForm(request.POST,instance = f)
      if form.is_valid():
         c = form.save()
         b = json.dumps({'comment':c.text, 'author':c.author.username, 'error':False})

   return HttpResponse(b,mimetype='application/json')
