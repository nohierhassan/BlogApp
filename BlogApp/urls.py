
from django.contrib import admin
from django.urls import path,include
from BlogApp import views

urlpatterns = [
<<<<<<< HEAD
    path('home/', views.home),	
    path('register/', views.register),	
    path('login/', views.login),		
=======
    path('home/', views.home,name='home'),	
    path('post/<id>', views.post),
    path('category/', views.category),
    path('blocked/', views.blocked),
    path('register/', views.register,name = 'register'),	
    path('login/', views.login),		

>>>>>>> 115849993d4e95e62b0c9902057d02de5d901ee8
]
