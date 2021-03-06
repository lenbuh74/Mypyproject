from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.OrderCreate, name='OrderCreate'),
    url(r'^admin/order/(?P<order_id>\d+)/$', views.AdminOrderDetail, name='AdminOrderDetail'),
    url(r'^customer/(?P<order_id>\d+)/$', views.CustomerOrderDetail, name='CustomerOrderDetail'),
    url(r'^customer/$', views.CustomerOrders, name='CustomerOrders'),
]
