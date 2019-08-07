from django.shortcuts import render, get_object_or_404
from .models import Client


def client_list(request):
    clients = Client.objects.all()
    clients = clients.filter(admin=request.user)
    return render(request, 'client/client_list.html', {
        'clients': clients
    })


def client_detail(request, phone):
    client = get_object_or_404(Client, phone=phone, admin=request.user)
    return render(request, 'client/client_detail.html', {
        'client': client
    })


def client_new(request):
    return render(request, 'client/client_new.html')


def client_edit(request):
    return render(request, 'client/client_edit.html')
