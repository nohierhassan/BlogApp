
from django.contrib import admin
from django.urls import path,include
from BlogApp import views

urlpatterns = [
    path('home/', views.home),	
    path('register/', views.register),	
    path('login/', views.login),		
]
