from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	context = {
	
	}
	return render(request ,'BlogApp/home.html' , context)

def register(request):
	context = {
	
	}
	return render(request ,'BlogApp/register.html' , context)


def login(request):
	context = {
	
	}
	return render(request ,'BlogApp/login.html' , context)

