from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from BlogApp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as authlogin
# Create your views here.
def home(request):
	context= {
	
	}
	return render(request ,'admin/index.html' , context)
def users(request):
	context= {
	
	}
	return render(request ,'admin/users.html' , context)
def posts(request):
	context= {
	
	}
	return render(request ,'admin/posts.html' , context)
def categories(request):
	context= {
	
	}
	return render(request ,'admin/categories.html' , context)
def forbiddenWords(request):
	context= {
	
	}
	return render(request ,'admin/forbiddenwords.html' , context)
