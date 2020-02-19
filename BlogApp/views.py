from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	context = {
	
	}
	return render(request ,'BlogApp/home.html' , context)


def post(request,id):
	# post = post.objects.get(id=id)
	context = {
				'id':id
	}

	return render(request,'BlogApp/post.html',context)


def category(request):
	context = {

	}
	return render (request,'BlogApp/category.html', context)

def blocked(request):
	context = {

	}
	return render (request, 'BlogApp/blocked.html', context)

def register(request):
	context = {
	
	}
	return render(request ,'BlogApp/register.html' , context)


def login(request):
	context = {
	
	}
	return render(request ,'BlogApp/login.html' , context)
