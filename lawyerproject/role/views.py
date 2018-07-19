from django.shortcuts import render
from django.shortcuts import redirect

from role.forms import RoleForm
from role.models import Role
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    results = Role.objects.all()
    data = {
        'results': results
    }
    return render(request, 'admin/role/index.html', data)


def create(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            data = Role.objects.create()
            data.role_name = request.POST['role_name']
            data.save()
            messages.success(request, 'Role has been successfully saved!')
            return redirect('role_index')
        else:
            content = {'form': form,'form_data': request.POST};
            return render(request, 'admin/role/create.html', content)
    else:
        return render(request, 'admin/role/create.html')


def update(request,id):
    editModeData = Role.objects.get(id=id)
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            editModeData.role_name = request.POST['role_name']
            editModeData.save()
            messages.success(request, 'Role has been successfully updated!')
            return redirect('role_index')
        else:
            content = {
                'form': form
            };
            return render(request, 'admin/role/edit.html', content)
    else:
        content = {'editModeData': editModeData, 'form_data': request.POST};
        return render(request, 'admin/role/edit.html',content)


def delete(request,id):

    try:
        results = Role.objects.get(id=id).delete()
        return HttpResponse('success')
    except Exception as e:
        return redirect('role_index')

