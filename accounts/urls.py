from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^login/$', views.signin, name='login'),
]
