from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import LawyerSerializer
from .models import Lawyer
from .forms import LawyerForm


class LawyerView(viewsets.ModelViewSet):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer


def index(request):
    return render(request, 'lawyer/lawyer-home.html')


def create_lawyer(request):
    return render(request, 'lawyer/create_lawyer.html')


def store_lawyer(request):
    if request.method == "POST":
        data = Lawyer.objects.create()
        data.lawyer_pic = request.FILES['lawyer_pic']
        data.first_name = request.POST['first_name']
        data.last_name = request.POST['last_name']
        data.speciality = request.POST['speciality']
        data.mobile_number = request.POST['mobile_number']
        data.email_address = request.POST['email_address']
        data.save()
        return redirect('create_lawyer')


def lawyer_list(request):
    lawyer = Lawyer.objects.all()
    return render(request, 'lawyer/lawyer_list.html', {'lawyer': lawyer})


def view_lawyer_update(request, id):
    lawyer = Lawyer.objects.get(id=id)
    form = LawyerForm(request.POST or None, instance=lawyer)

    if form.is_valid():
        form.save()
        return redirect('lawyer_list')

    return render(request, 'lawyer/update-lawyer.html', {'form': form, 'lawyer': lawyer})


def delete_lawyer(request, id):

    try:
        results = Lawyer.objects.get(id=id).delete()
        return HttpResponse('success')
    except Exception as e:
        return redirect('lawyer_list')


def update_form_action_lawyer(request, id):
    lawyer = Lawyer.objects.get(id=id)
    if request.method == "POST":
        form = LawyerForm(request.POST or None, request.FILES, instance=lawyer)
        # lawyer.lawyer_pic = request.FILES['lawyer_pic']
        # lawyer.first_name = request.POST['first_name']
        # lawyer.last_name = request.POST['last_name']
        # lawyer.speciality = request.POST['speciality']
        # lawyer.mobile_number = request.POST['mobile_number']
        # lawyer.email_address = request.POST['email_address']
        if form.is_valid():
            form.save()
            return redirect('lawyer_list')

    context = {
        'lawyer': lawyer,
        'form': form
    }

    return render(request, 'lawyer/update-lawyer.html', context)
