from django.db import models
from django.conf import settings


class Business(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Client(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    content = models.TextField(blank=True, null=True)

    # business 휴대폰
    call_plane = models.CharField(max_length=50, blank=True, null=True)
    resident_registration_number = models.CharField(max_length=50, blank=True, null=True)
    birth = models.CharField(max_length=50, blank=True, null=True)
    agent = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    agent_phone = models.CharField(max_length=15, blank=True, null=True)
    joining_date = models.CharField(max_length=50, blank=True, null=True)
    division = models.CharField(max_length=50, blank=True, null=True)
    note1 = models.CharField(max_length=50, blank=True, null=True)
    note2 = models.CharField(max_length=50, blank=True, null=True)
    note3 = models.CharField(max_length=50, blank=True, null=True)
    registration_date = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
