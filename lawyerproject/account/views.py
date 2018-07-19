from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard_index')
    else:
        form = UserCreationForm()
    data = {'form': form}
    return render(request, 'account/signup.html', data)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('dashboard_index')
    else:
        form = AuthenticationForm()
    data = {'form': form}
    return render(request, 'account/login.html', data)


def logout_view(request):
    logout(request)
    try:
        messages.success(request, 'Your have been successfully logged out!')
        return redirect('accounts:login')
    except Exception as e:
        messages.warning(request, 'Your are not logged out due to an error: {}'.format(e))
    return redirect('posts:post_list')

