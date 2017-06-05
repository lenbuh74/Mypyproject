from django.conf.urls import url,include
from . import views
from .views import *

urlpatterns = [
    url(r'^$', views.ProductList, name='ProductList'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^', include('registration.urls')),
    #url(r"^$", archive),
    #(r"^comments/", include("django.contrib.comments.urls")),
    ]