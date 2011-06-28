import os
import sys

path = '/home/searchinit'
if path not in sys.path:
   sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'searchSite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
