from django.shortcuts import render, redirect

from users.forms import UserForm
from users.models import User
from role.models import Role
from django.http import HttpResponse
from users.forms import UserForm



def index(request):
    users = User.objects.all()
    return render(request, "admin/users/index.html", {'users': users})


def create(request):
    roles = Role.objects.all()
    return render(request, "admin/users/create.html", {'roles': roles})


def store(request):
    roles = Role.objects.all()
    if request.method == "POST":
        data = User.objects.create()
        data.full_name = request.POST['full_name']
        data.email = request.POST['email']
        data.password = request.POST['password']
        data.role_id = request.POST['role_id']
        data.status = request.POST['status']
        data.save()
        return redirect('user_index')

    else:
        return render(request, 'admin/users/create.html', {'roles': roles})


def edit(request, id):
    edit_mode_data = User.objects.get(id=id)
    roles = Role.objects.all()
    return render(request, "admin/users/edit.html", {'roles': roles, 'edit_mode_data': edit_mode_data})


def update(request,id):

    editModeData = User.objects.get(id=id)
    if request.method == "POST":
        editModeData.full_name = request.POST['full_name']
        editModeData.email = request.POST['email']
        editModeData.role_id = request.POST['role_id']
        editModeData.status = request.POST['status']
        editModeData.save()

        return redirect('user_index')
    else:
        content = {'editModeData': editModeData, 'form_data': request.POST};
        return render(request, 'admin/users/edit.html',content)


def delete(request, id):

    try:
        results = User.objects.get(id=id).delete()
        return HttpResponse('success')
    except Exception as e:
        return redirect('user_index')

