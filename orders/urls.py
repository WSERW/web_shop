from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^create_request/$', views.call_request_create, name='request_create'),
]
