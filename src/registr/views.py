from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError


def home(request):
    return render(request, 'registr/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'registr/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'registr/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'Такой имя ползавателя ужи сушестует'})

        else:
            return render(request, 'registr/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Парол не совпадает'})


def user_login(request):
    if request.method == "GET":
        return render(request, 'registr/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'registr/login.html',
                          {'form': AuthenticationForm(), 'error': 'Неверний данний для входа'})

        else:
            login(request, user)
            return redirect('index')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
