
from django.views.generic import TemplateView, DetailView

from django.http import HttpResponseRedirect
from searchSite.recapForm import ReCaptchaField

from django.contrib.auth  import login, authenticate

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from searchSite.annoying.decorators import render_to

class ProfileView(TemplateView):
   template_name = "accounts/myprofile.html"

class ProfileSpecificView(DetailView):
   template_name = "accounts/profile.html"
   model = User

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
