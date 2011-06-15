from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Template
from django.views.generic import TemplateView

from django.shortcuts import render_to_response

from django.forms import ModelForm, PasswordInput, DateInput
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from recapForm import ReCaptchaField


class IndexView(TemplateView):
   template_name= "index.html"

class MyCreationForm(UserCreationForm):
   captcha = ReCaptchaField()

def register(request):
   if request.method == 'POST':

      temp = request.POST.copy()
      temp['REMOTE_ADDR'] = request.META['REMOTE_ADDR']
      form = MyCreationForm(data=temp)
      if form.is_valid():
         username = form.cleaned_data['username']
         password =  form.cleaned_data['password1']
         User.objects.create_user(username,"",password)

         return HttpResponseRedirect('/thanks/')

   else:
      form = MyCreationForm()

   return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))

