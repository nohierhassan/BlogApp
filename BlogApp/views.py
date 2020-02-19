from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as authlogin
# Create your views here.

def home(request):
	context = {
	
	}
	return render(request ,'BlogApp/home.html' , context)

<<<<<<< HEAD
def register(request):
	context = {
	
	}
	return render(request ,'BlogApp/register.html' , context)
=======

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
	if request.method == 'POST':

		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username, password = password)
			authlogin(request,user)
			return redirect('home')
	else:

		form = UserCreationForm()
	context = {

		'form':form
	}
	return render(request ,'registration/register.html' , context)
>>>>>>> 115849993d4e95e62b0c9902057d02de5d901ee8


def login(request):
	context = {
	
	}
	return render(request ,'BlogApp/login.html' , context)

