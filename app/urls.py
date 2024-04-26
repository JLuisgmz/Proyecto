from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('salir/', views.salir, name='salir'),
    path('registrar/', views.registrarUN, name='registrarUN'),
    path('registrarE/', views.registrarUE, name='registrarUE'),
    path('listadoN/', views.listadoN, name='listadoN'),
    path('listadoE/', views.listadoE, name='listadoE'),
    path('eliminar/', views.eliminarN, name='eliminar'),
    path('editarN/', views.eliminarN, name='editarN'),
    path('registere/', views.signupe, name='registere'),
    path('registern/', views.signupn, name='registern'),

    path('login_view/', views.login_view, name='login_view'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('find_user_view/', views.find_user_view, name='find_user_view'),
    path('home_view/', views.home_view, name='home_view'),



]
