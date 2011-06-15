from django.db import models
from django.contrib import auth

from django.db.models.signals import post_save

from django.forms import ModelForm

class Tag(models.Model):
   name = models.CharField(max_length = 30)

   def __unicode__(this):
      return this.name

   def get_absolute_url(this):
      return '/articles/tags/%d' % this.pk


class Article(models.Model):
   name = models.CharField(max_length = 30)
   author  = models.ForeignKey(auth.models.User)
   tag = models.ForeignKey(Tag)
   text = models.TextField()

   def __unicode__(this):
      return this.name

   def get_absolute_url(this):
      return '/articles/%d' % this.pk

class CreateArticleForm(ModelForm):
   class Meta:
      model = Article
      fields = ('name','tag','text')

class Comment(models.Model):
   text = models.TextField()
   article = models.ForeignKey(Article)

   def __unicode__(this):
      return this.text

class UserProfile(models.Model):
   user = models.OneToOneField(auth.models.User)
   specialty = models.CharField(max_length = 30)

   def __unicode__(this):
      return u'The profile for %s' % this.user

def create_user_profile(sender,instance,created,**kwargs):
   if created:
      profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile,sender=auth.models.User)



