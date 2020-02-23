from django.contrib import admin
from django.urls import path,include
from .views import (
	registration_view,
	LoginVeiw,
	LogoutView,
	EditView
	)


urlpatterns = [
    path('register/', registration_view, name = "register"),	
    path('login/', LoginVeiw, name = "login"),
    path('logout/', LogoutView, name = "logout"),
    path('edit/', EditView, name = "edit"),
]