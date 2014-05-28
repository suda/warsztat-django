try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from . import views

urlpatterns = patterns('',
    url(r'^$', views.hello, name='hello'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^(?P<name>[\w]+)/$', views.hello_name, name='hello_name'),    
)
