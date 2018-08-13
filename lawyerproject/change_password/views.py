from django.shortcuts import render,redirect
from users.models import User
from django.http import HttpResponse

# Create your views here.
def create(request):

    return render(request, "admin/change_password/change_password.html")

#
# def update(request):
#
#     editModeData = User.objects.get( =request.POST['email'])
#     if request.method == "POST":
#         editModeData.password = request.POST['password']
#         editModeData.save()
#         return redirect('change_password')
#     else:
#         return render(request, "admin/change_password/change_password.html")
