from .forms import UserRegistrationForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def user_login(request):
    return render(request, 'login.html')

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('login:show_user'))
    return HttpResponseRedirect(reverse('login:user_login'))

@login_required
def show_user(request):
    return render(request, 'login/user.html', {
        "username": request.user.username,
    })

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('login:show_user'))
    else:
        form = UserRegistrationForm()

    return render(request, 'login/register.html', {
        'form': form,
    })

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:user_login'))
