from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as authlogin
from .models import *
from django.db.models import Q 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
User = settings.AUTH_USER_MODEL
# Create your views here.
# @login_required
def home(request):

	# query: get all posts
	topPosts= Post.objects.all().order_by('-postDatePublished')[:5] 
	all_categories= Category.objects.all()
	sub_cat=Category.objects.filter(userId=request.user.id)

	context = {"topPosts": topPosts, "all_categories":all_categories, "sub_cat":sub_cat}
	# context = {"topPosts": topPosts, "all_categories":all_categories}
	return render(request ,'BlogApp/index.html' , context)



def post(request,id):
	# post = post.objects.get(id=id)
	# query = request.GET.get("q,None")
	# qs = Post.objects.all()
	# if query is not None:
	# 	qs = qs.filter(
	# 		Q(title__icontains=query)

	# 	).distinct()
	

	context = {
				'postId':id,
				#'object_list': qs,
	}

	return render(request,'BlogApp/post.html',context)

def search(request):
	query = request.GET.get("q")
	#qs = Post.objects.all()
	if query :
		qs = Post.objects.filter(
			Q(title__icontains=query)

		).distinct()
	

	context = {
				'object_list': qs,
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


def login(request):
	context = {
	
	}
	return render(request ,'BlogApp/login.html' , context)

def showpost(request,num):
	post=Post.objects.get(pk=num)
	

	return render(request,'post/post.html',{'post':post})
	
# def subscribe(request, numb):
# 	subcat = Category.objects.get(categoryId=numb)

# 	if request.POST.get('subscribe') == '0':
# 	   subcat.userId.remove(request.user)
# 	else:
# 		subcat.userId.add(request.user)

# 	return HttpResponseRedirect('/blog/home')
def subscribe(request, numb):
	subcat = Category.objects.get(categoryId=numb)

	if request.POST.get('subscribe') == '0':
	   subcat.userId.remove(request.user)
	else:
		subcat.userId.add(request.user)

	return HttpResponseRedirect('/blog/home')
	



	
# def subscribe(request):
#     w = user.objects.get(id=request.POST['id'])
#     w.is_working = request.POST['isworking'] == 'true'
#     w.save()
#     return HttpResponse('success')