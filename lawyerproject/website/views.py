from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import (View, TemplateView, CreateView)
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User


def index(request):
    return render(request, 'website/index.html')


# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('dashboard_index')
#     else:
#         form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'website/signup.html', context)


class SignUpView(CreateView):
    template_name = 'website/signup.html'
    form_class = UserCreationForm

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('posts:post_list')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'website/login.html', context)
