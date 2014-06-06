from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag()
def witaj(name):
	return mark_safe(u'Witaj %s' % name)

@register.filter
def dodaj_wykrzyknik(tekst):
    return u'%s!' % unicode(tekst)