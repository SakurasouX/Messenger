from django.shortcuts import render
from django.http import HttpResponse


def user_login(request):
    return render(request, 'accounts/login.html')


def user_registration(request):
    return render(request, 'accounts/registration.html')
