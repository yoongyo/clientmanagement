from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from .models import Client, Business
from django.contrib.auth.decorators import login_required
from .forms import ClientForm
import openpyxl
import re


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


def client_detail(request, user_id, user_ps, phone):
    client = get_object_or_404(Client, phone=phone, admin__username=user_id)
    clientId = client.pk
    return render(request, 'client/client_detail.html', {
        'client': client,
        'user_id': user_id,
        'user_ps': user_ps,
        'clientId': clientId,
    })


def client_new(request):
    ok = True
    validation = ""
    clients = Client.objects.all()
    clients = clients.filter(admin=request.user)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save(commit=False)
            client.admin = request.user
            for i in clients:
                if i.phone == client.phone:
                    validation = "이미 저장된 번호입니다."
                    ok = False
            if ok:
                client.save()
                return HttpResponseRedirect(reverse('client:client_detail', args=[request.user.username,
                                                                                  request.user.password,
                                                                                  client.phone]))
        else:
            print(form.errors)
    else:
        form = ClientForm()
    return render(request, 'client/client_new.html', {
        'form': form,
        'validation': validation
    })


def client_edit(request, phone):
    ok = True
    validation = ""
    clients = Client.objects.all()
    clients = clients.filter(admin=request.user)
    client = get_object_or_404(Client, admin=request.user, phone=phone)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.admin = request.user
            client.save()
            return HttpResponseRedirect(reverse('client:client_detail', args=[request.user.username,
                                                                              request.user.password,
                                                                              client.phone]))
        else:
            print(form.errors)
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/client_edit.html', {
        'form': form,
        'validation': validation
    })


def excel(request):
    if request.method == "POST":
        excel = request.FILES['file']
        print(excel)
        wb = openpyxl.load_workbook(excel)
        ws = wb.active
        for r in ws.rows:
            name = r[2].value
            resident_registration_number = r[3].value
            address = r[4].value
            phone2 = r[5].value
            agent = r[6].value
            agent_phone = r[7].value
            call_plane = r[8].value
            joining_date = r[9].value
            note1 = r[10].value
            note2 = r[11].value
            note3 = r[12].value
            division = r[13].value
            registration_date = r[14].value
            if phone2 == "":
                phone = ""
            else:
                phone = re.sub('[-]', '', phone2)
            print(phone)
            model_instance = Client(business=Business.objects.all()[0], admin=request.user, name=name, phone2=phone2,
                                    resident_registration_number=resident_registration_number, address=address,
                                    phone=phone, agent=agent, agent_phone=agent_phone, call_plane=call_plane,
                                    joining_date=joining_date, note1=note1, note2=note2, note3=note3, division=division,
                                    registration_date=registration_date)
            model_instance.save()
    return render(request, 'client/excel.html')


def client_delete(request, user_id, user_ps, id):
    client = get_object_or_404(Client, pk=id)
    client.delete()
    return HttpResponseRedirect(reverse('client:client_list'))
