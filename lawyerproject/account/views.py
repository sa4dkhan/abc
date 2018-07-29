from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


def signup_view(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user #relation of profile with user

            if 'profile_pics' in request.FILES:
                profile.profile_pics = request.FILES['profile_pics']

            profile.save()
            login(request, user)
            return redirect('dashboard_index')

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'account/signup.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard_index'))

            else:
                return HttpResponse("Account not active")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied")

    else:
        return render(request, 'account/login.html', {})


@login_required
def logout_view(request):
    logout(request)
    try:
        messages.success(request, 'Your have been successfully logged out!')
        return redirect('accounts:login')
    except Exception as e:
        messages.warning(request, 'Your are not logged out due to an error: {}'.format(e))
    return redirect('dashboard_index')

