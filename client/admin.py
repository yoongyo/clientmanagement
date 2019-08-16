from django.contrib import admin
from . models import Client, Business


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']


class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Business, BusinessAdmin)
admin.site.register(Client, ClientAdmin)