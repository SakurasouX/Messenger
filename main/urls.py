from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='main'),
    path('home', views.home, name='home'),
    path('search', views.search, name='search'),
]
