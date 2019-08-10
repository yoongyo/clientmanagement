from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from .models import Client
from django.contrib.auth.decorators import login_required
from .forms import ClientForm


@login_required()
def client_list(request):
    user_id = request.user.username
    user_ps = request.user.password
    clients = Client.objects.all()
    clients = clients.filter(admin=request.user)
    return render(request, 'client/client_list.html', {
        'clients': clients,
        'user_id': user_id,
        'user_ps': user_ps
    })


def client_detail(request, phone):
    client = get_object_or_404(Client, phone=phone, admin=request.user)
    return render(request, 'client/client_detail.html', {
        'client': client
    })


def client_new(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save(commit=False)
            client.admin = request.user
            client.save()
            return HttpResponseRedirect(reverse('client:client_detail', args=[client.phone]))
        else:
            print(form.errors)
    else:
        form = ClientForm()
    return render(request, 'client/client_new.html', {
        'form': form,
    })


def client_edit(request, phone):
    client = get_object_or_404(Client, admin=request.user, phone=phone)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.admin = request.user
            client.save()
            return HttpResponseRedirect(reverse('client:client_detail', args=[client.phone]))
        else:
            print(form.errors)
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/client_edit.html', {
        'form': form,
    })
