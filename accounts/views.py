from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        return HttpResponseRedirect('/')
    else:
        return render(request, 'accounts/login.html')


def user_registration(request):
    return render(request, 'accounts/registration.html')
