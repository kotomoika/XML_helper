__author__ = 'kat'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^xpath', views.xpath, name='xpath'),
    url(r'^new', views.result_handler, name='new'),
    url(r'^contact', views.contact, name='contact'),
    #url(r'^xmlnew', views.xmlnew, name='xmlnew'),
    #url(r'^xpathhandler/', views.xpathhandler, name='xpathhandler'),
]