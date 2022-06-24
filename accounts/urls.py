from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('registration', views.user_registration, name='registration'),
    path('logout', views.user_logout, name='logout'),
]