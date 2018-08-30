from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() # load the profile instance created by the signal
            user.profile.phone = form.cleaned_data.get('phone')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('dashboard_index')

    else:
        form = SignUpForm()
    return render(request, 'account/signup.html',{'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard_index')
    else:
        form = AuthenticationForm()
    data = {'form': form}
    return render(request, 'account/login.html', data)


@login_required
def logout_view(request):
    logout(request)
    try:
        messages.success(request, 'Your have been successfully logged out!')
        return redirect('accounts:login')
    except Exception as e:
        messages.warning(request, 'Your are not logged out due to an error: {}'.format(e))
    return redirect('dashboard_index')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #important
            messages.success(request, 'Your password successfully updated!')
            return redirect('account:login')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form})

