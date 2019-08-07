from django.contrib import admin
from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.client_list, name='client_list'),
    re_path(r'^(?P<phone>\d{3}\d{3,4}\d{4})/$', views.client_detail, name='client_detail'),
    re_path(r'^new$', views.client_new, name='client_new'),
    re_path(r'^(?P<phone>\d{3}\d{3,4}\d{4})/edit/$', views.client_edit, name='client_edit'),
]
