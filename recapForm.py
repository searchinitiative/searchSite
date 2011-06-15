from django import forms
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_unicode

import settings

import urllib
import urllib2


class ReCaptchaWidget(forms.Widget):

   def get_recaptcha_widget_html(self, field_name):
      widget = u''
      widget += u'<div class="recaptcha_box" id="fdiv_%s"></div>' % field_name
      widget += u'<script type="text/javascript" src="http://www.google.com/recaptcha/api/js/recaptcha_ajax.js"></script>'
      widget += u'<script type="text/javascript">'
      widget += u'Recaptcha.create("%s", "fdiv_%s", {theme: "white"});' % (settings.RECAPTCHA_PUBKEY, field_name)
      widget += u'</script>'
      
      return widget
      
   def value_from_datadict(self, data, files, name):
      
      remoteip = None
      
      remoteip = data.get('REMOTE_ADDR')
      
      return {
         'challenge' : data.get('recaptcha_challenge_field', None), 
         'response' : data.get('recaptcha_response_field', None),
         'remoteip' : remoteip
      }
   
   def render(self, name, value, attrs=None):
      return mark_safe(self.get_recaptcha_widget_html(name))
      
class ReCaptchaField(forms.Field):

   widget = ReCaptchaWidget
   required = True
   
   def verify_captcha(self, challenge, response,remoteip):
      url = 'http://www.google.com/recaptcha/api/verify'
      values = {
         'privatekey': settings.RECAPTCHA_PRIVKEY, 
         'challenge' : challenge, 
         'response' : response
      }
      
      values['remoteip'] = remoteip
         
      vrequest = urllib2.Request(url, urllib.urlencode(values))
      vresponse = urllib2.urlopen(vrequest)
      result = vresponse.read().split('\n')
      
      if result[0] == 'true':
         return (True, result[1])
         
      return (False, result[1])
      
   def clean(self, value):
      super(ReCaptchaField, self).clean(value['response'])
      
      result = self.verify_captcha(value['challenge'], value['response'], value['remoteip'])
      
      if not result[0]:
         raise forms.ValidationError('Wrong answer, try again.')
      
      return value['response']

      
class ReCaptchaForm(forms.Form):
   
   def __init__(self, data=None, remoteip=None, *args, **kwargs):
      if data and remoteip:
         data = data.copy()
         data['REMOTE_ADDR'] = remoteip
         
      super(ReCaptchaForm, self).__init__(data=data, *args, **kwargs)
