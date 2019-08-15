from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path(r'^$', views.main, name='main'),
    re_path(r'^info/$', views.info, name='info'),
    path('admin/', admin.site.urls),
    path('client/', include(('client.urls', 'client'), namespace='client')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
