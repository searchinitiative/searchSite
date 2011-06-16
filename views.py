from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Template
from django.views.generic import TemplateView, DetailView

from django.forms import ModelForm, PasswordInput, DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth  import login, authenticate

from recapForm import ReCaptchaField

from searchSite.annoying.decorators import render_to


class ProfileView(TemplateView):
   template_name = "accounts/myprofile.html"

class ProfileSpecificView(DetailView):
   template_name = "accounts/profile.html"
   model = User

class IndexView(TemplateView):
   template_name= "index.html"

class NewsView(TemplateView):
   template_name= "news.html"

class MyCreationForm(UserCreationForm):
   captcha = ReCaptchaField()

@render_to("accounts/register.html")
def register(request):
   if request.method == 'POST':

      temp = request.POST.copy()
      temp['REMOTE_ADDR'] = request.META['REMOTE_ADDR']
      form = MyCreationForm(data=temp)
      if form.is_valid():
         username = form.cleaned_data['username']
         password =  form.cleaned_data['password1']

         User.objects.create_user(username,"",password)
         
         login(request,authenticate(username=username,password=password))

         return HttpResponseRedirect('/accounts/profile')

   else:
      form = MyCreationForm()

   return  {'form':form}

