from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm
from django.http import HttpResponse
from pprint import pprint
from django.http import JsonResponse
from django.template.loader import render_to_string


def index(request):
    return render(request, 'admin/admin-home.html')


def client_dashboard(request, id):
    client = Client.objects.get(id=id)
    return render(request, 'clients/client-home.html', {'client': client})


def client_info(request):
    form = ClientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('admin/admin-home.html')

    return render(request, 'clients/client.html', {'form': form})


def store_client(request):
    if request.method == "POST":
        data = Client.objects.create()
        data.client_pic = request.FILES['client_pic']
        data.first_name = request.POST['first_name']
        data.last_name = request.POST['last_name']
        data.mobile_number = request.POST['mobile_number']
        data.email_address = request.POST['email_address']
        data.save()
        return redirect('client_list')


def client_list(request):
    client = Client.objects.all()
    # return HttpResponse(client.all().First_Name)
    return render(request, 'clients/client_list.html', {'client': client})


def update_client(request, id):
    client = Client.objects.get(id=id)
    # pprint(dir(client))
    # print(object.__dict__)
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('client_list')

    return render(request, 'clients/update-client.html', {'form': form, 'client': client})


def update_form_action(request,id):

    client = Client.objects.get(id=id)
    form = ClientForm(request.POST or None, instance=client)
    if request.method == "POST":
        client.client_pic = request.FILES['client_pic']
        client.first_name = request.POST['first_name']
        client.last_name = request.POST['last_name']
        client.mobile_number = request.POST['mobile_number']
        client.email_address = request.POST['email_address']
        client.save()
        return redirect('client_list')

    return render(request, 'clients/update-client.html', {'form': form, 'client': client})


# def delete_client(request, id):
#     client = Client.objects.get(id=id)
#
#     if request.method == 'POST':
#         client.delete()
#         return redirect('client_list')
#
#     return render(request, 'clients/delete-client-form.html', {'client': client})


def delete_client(request, id):

    try:
        results = Client.objects.get(id=id).delete()
        return HttpResponse('success')
    except Exception as e:
        return redirect('client_list')


