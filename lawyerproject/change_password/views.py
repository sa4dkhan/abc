from django.shortcuts import render
from users.models import User

# Create your views here.
def create(request):

    return render(request, "admin/change_password/change_password.html")


def update(request):

    editModeData = User.objects.get(email=request.POST['email'])
    if request.method == "POST":

        editModeData.status = request.POST['status']
        editModeData.save()

        return redirect('user_index')
    else:
        content = {'editModeData': editModeData, 'form_data': request.POST};
        return render(request, 'admin/users/edit.html',content)
