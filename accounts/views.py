from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def user_login(request):
    """User login"""
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('main:home'))
        else:
            return HttpResponse()
    else:
        return render(request, 'accounts/login.html')


def user_logout(request):
    """User logout"""
    logout(request)
    return HttpResponseRedirect(reverse('main:home'))


def user_registration(request):
    """
    Create new user
    """
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password_confirm')
        try:
            if password == confirm_password:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                login(request, user)
                return HttpResponseRedirect(reverse('main:home'))
            else:
                context = {
                    'password': 'Пароли не совпадают',
                    'username': None,
                }
                return render(request, 'accounts/registration.html', context)
        except ValueError:
            context = {
                'username': 'Введите имя пользователя',
                'password': None,
            }
            return render(request, 'accounts/registration.html', context)
    else:
        return render(request, 'accounts/registration.html')
