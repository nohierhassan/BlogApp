from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from BlogApp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as authlogin
from adminUser.forms import *
from AccountsApp.models import ExtendedUser

from django.conf import settings


from django.contrib.auth.decorators import login_required

# Create your views here.

def admin_only(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_admin:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('adminlogin')
    return wrap

@admin_only
def home(request):
	user = request.user
	context= {'user' : user} 
	return render(request ,'admin/index.html' , context)
@admin_only
def users(request):
	users = ExtendedUser.objects.all()
	context = {'all_users' : users}
	return render(request ,'admin/users.html' , context)
@admin_only
def posts(request):
	posts = Post.objects.all()
	context = {'all_posts' : posts}
	return render(request ,'admin/posts.html' , context)
@admin_only
def categories(request):
	category = Category.objects.all()
	context = {'all_categories' : category}
	return render(request ,'admin/categories.html' , context)
@admin_only
def forbiddenWords(request):
	words = ForbiddenWord.objects.all()
	context = {'all_words' : words}
	return render(request ,'admin/forbiddenwords.html' , context)
@admin_only
def editWord(request,num):
    wd = ForbiddenWord.objects.get(wordId = num)
    if(request.method == 'POST'):
        wd_form = WordForm(request.POST, instance = wd)
        if wd_form.is_valid():
            wd_form.save()
            return HttpResponseRedirect('/adminUser/forbiddenwords/') 
    else:
        wd_form = WordForm(instance = wd)
        context = {'wd_form':wd_form}
        return render(request,'admin/wd_add.html',context)
@admin_only
def deleteWord(request,num):
    wd = ForbiddenWord.objects.get(wordId = num)
    wd.delete()
    return HttpResponseRedirect('/adminUser/forbiddenwords/') 
@admin_only
def addWord(request):
	wd_form = WordForm()
	if(request.method == 'POST'):
		wd_form = WordForm(request.POST)
		if wd_form.is_valid():
			wd_form.save()
			return HttpResponseRedirect('/adminUser/forbiddenwords/')
	else:
		context = {'wd_form': wd_form}
		return render(request,'admin/wd_add.html',context)

@admin_only
def editCategory(request,num):
    cat = Category.objects.get(categoryId = num)
    if(request.method == 'POST'):
        cat_form = CategoryForm(request.POST, instance = cat)
        if cat_form.is_valid():
            cat_form.save()
            return HttpResponseRedirect('/adminUser/categories/') 
    else:
        cat_form = CategoryForm(instance = cat)
        context = {'cat_form':cat_form}
        return render(request,'admin/cat_add.html',context)
@admin_only
def deleteCategory(request,num):
    cat = Category.objects.get(categoryId = num)
    cat.delete()
    return HttpResponseRedirect('/adminUser/categories/') 

@admin_only
def addCategory(request):
	cat_form = CategoryForm()
	if(request.method == 'POST'):
		cat_form = CategoryForm(request.POST)
		if cat_form.is_valid():
			cat_form.save()
			return HttpResponseRedirect('/adminUser/categories/')
	else:
		context = {'cat_form': cat_form}
		return render(request,'admin/cat_add.html',context)

@admin_only
def addPost(request):
	post_form = PostForm()
	if(request.method == 'POST'):
		post_form = PostForm(request.POST,request.FILES)
		if post_form.is_valid():
			newForm = post_form.save(commit=False)
			newForm.postAuthor = request.user
			newForm.save()
			post_form.save()
			return HttpResponseRedirect('/adminUser/posts/')
	else:
		context = {'post_form': post_form}
		return render(request,'admin/post_add.html',context)

@admin_only
def deletePost(request,num):
    pt = Post.objects.get(postId = num)
    pt.delete()
    return HttpResponseRedirect('/adminUser/posts/') 
@admin_only
def editPost(request,num):
    pt = Post.objects.get(postId = num)
    if(request.method == 'POST'):
        post_form = PostForm(request.POST, instance = pt)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect('/adminUser/posts/') 
    else:
        post_form = PostForm(instance = pt)
        context = {'post_form':post_form}
        return render(request,'admin/post_add.html',context)
		
@admin_only
def addUser(request):
	user_form = UserForm()
	if(request.method == 'POST'):
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect('/adminUser/users/')
		else:
			context = {}
			return render(request,'admin/auth_error.html',context)


	else:
		context = {'user_form': user_form}
		return render(request,'admin/user_add.html',context)
@admin_only
def deleteUser(request,num):
	us = ExtendedUser.objects.get(id = num)
	us.delete()
	return HttpResponseRedirect('/adminUser/users/') 
@admin_only
def editUser(request,num):
    us = ExtendedUser.objects.get(id = num)
    if(request.method == 'POST'):
        user_form = UserForm(request.POST, instance = us)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('/adminUser/users/') 
    else:
        user_form = UserForm(instance = us)
        context = {'user_form':user_form}
        return render(request,'admin/user_add.html',context)

@admin_only

def addTag(request):
	tag_form = TagForm()
	if(request.method == 'POST'):
		tag_form = TagForm(request.POST)
		if tag_form.is_valid():
			tag_form.save()
			return HttpResponseRedirect('/adminUser/posts/addTag')
	else:
		context = {'tag_form': tag_form}
		return render(request,'admin/tag_add.html',context)
@admin_only
def isAdmin(request, num):
	us = ExtendedUser.objects.get(id = num)
	us.is_admin = True
	us.is_superuser = True
	us.is_staff = True
	us.save()
	return HttpResponseRedirect('/adminUser/users/') 
@admin_only
def blocked(request, num):  
	us = ExtendedUser.objects.get(id = num)
	us.is_blocked = True
	us.save()
	return HttpResponseRedirect('/adminUser/users/')

@admin_only
def unblocked(request, num):
	us = ExtendedUser.objects.get(id = num)
	us.is_blocked = False
	us.save()
	return HttpResponseRedirect('/adminUser/users/')



