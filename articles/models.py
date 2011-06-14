from django.db import models
from django.contrib import auth

class Tag(models.Model):
   name = models.CharField(max_length = 30)

   def __unicode__(this):
      return this.name

class Article(models.Model):
   name = models.CharField(max_length = 30)
   author  = models.ForeignKey(auth.models.User)
   tag = models.ForeignKey(Tag)

   def __unicode__(this):
      return this.name




