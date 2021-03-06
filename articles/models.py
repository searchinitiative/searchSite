from django.db import models
from django.contrib import auth
from django.forms import ModelForm, CharField
from django import forms

from searchSite.annoying.fields import AutoOneToOneField

class Tag(models.Model):
   name = models.CharField(max_length = 30,unique=True)

   def __unicode__(this):
      return this.name

   def get_absolute_url(this):
      return '/articles/tags/%d' % this.pk


class Article(models.Model):
   name = models.CharField(max_length = 30,unique=True)
   author  = models.ForeignKey(auth.models.User)
   tag = models.ForeignKey(Tag)
   text = models.TextField()

   def canEdit(user):
      return user == author

   def __unicode__(this):
      return this.name

   def get_absolute_url(this):
      return '/articles/%d' % this.pk

class CreateArticleForm(ModelForm):
   class Meta:
      model = Article
      fields = ('name','tag','text')

class EditArticleForm(ModelForm):
   class Meta:
      model = Article
      fields = ('text',)


class Comment(models.Model):
   text = models.TextField()
   article = models.ForeignKey(Article)
   author = models.ForeignKey(auth.models.User)

   def __unicode__(this):
      return this.text

class EditCommentForm(ModelForm):
   class Meta:
      model = Comment
      fields = ('text',)

class CreateCommentForm(ModelForm):
   class Meta:
      model = Comment
      fields = ('text',)

class UserProfile(models.Model):
   user = AutoOneToOneField(auth.models.User, primary_key=True)
   specialty = models.CharField(max_length = 30)

   def __unicode__(this):
      return u'The profile for %s' % this.user




