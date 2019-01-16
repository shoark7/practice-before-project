from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import UserLoginForm, UserCreationForm


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def log_in(request):
    if request.method == 'GET':
        form = UserLoginForm()
    elif request.method == 'POST':
        user_identifier = request.POST['user_identifier']
        password = request.POST['password']
        user = authenticate(request, user_identifier=user_identifier, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            form = UserLoginForm(request)

    return render(request, 'user/login-page.html', {'form': form})


def sign_in(request):
    if request.method == 'GET':
        form = UserCreationForm()
    elif request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'user/signin-page.html', {'form': form})
