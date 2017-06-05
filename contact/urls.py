from django.conf.urls import url,include

from .views import *

urlpatterns = [

    url(r'^contact/$', contactform, name='contact'),
    url(r'^thanks/$', thanks, name='thanks'),
    ]