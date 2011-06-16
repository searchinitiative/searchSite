from django import template
from django.template.defaultfilters import *

from searchSite.util import *

register = template.Library()


@register.filter
@stringfilter
def xsscheck(html):
   "Does an xss filter"
   return mark_safe(sanitizeHtml(html))
