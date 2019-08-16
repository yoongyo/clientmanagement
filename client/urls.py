from django.contrib import admin
from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.client_list, name='client_list'),
    re_path(r'^(?P<user_id>\w+)/(?P<user_ps>[\w|\W]+)/(?P<phone>[\w|\W]+)/$', views.client_detail, name='client_detail'),
    re_path(r'^new$', views.client_new, name='client_new'),
    re_path(r'^(?P<phone>[\w|\W]+)/edit/$', views.client_edit, name='client_edit'),
    re_path(r'^excel/$', views.excel, name='excel')
]
