from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from BlogApp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as authlogin
from adminUser.forms import *
from AccountsApp.models import ExtendedUser
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
	context= {
	
	}
	return render(request ,'admin/index.html' , context)
@login_required
def users(request):
	users = ExtendedUser.objects.all()
	context = {'all_users' : users}
	return render(request ,'admin/users.html' , context)
@login_required
def posts(request):
	posts = Post.objects.all()
	context = {'all_posts' : posts}
	return render(request ,'admin/posts.html' , context)
@login_required
def categories(request):
	category = Category.objects.all()
	context = {'all_categories' : category}
	return render(request ,'admin/categories.html' , context)
@login_required
def forbiddenWords(request):
	words = ForbiddenWord.objects.all()
	context = {'all_words' : words}
	return render(request ,'admin/forbiddenwords.html' , context)

@login_required
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
@login_required
def deleteWord(request,num):
    wd = ForbiddenWord.objects.get(wordId = num)
    wd.delete()
    return HttpResponseRedirect('/adminUser/forbiddenwords/') 
@login_required
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

@login_required
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

@login_required
def deleteCategory(request,num):
    cat = Category.objects.get(categoryId = num)
    cat.delete()
    return HttpResponseRedirect('/adminUser/categories/') 

@login_required
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

@login_required
def addPost(request):
	post_form = PostForm()
	if(request.method == 'POST'):
		post_form = PostForm(request.POST,request.FILES)
		if post_form.is_valid():
			post_form.save()
			return HttpResponseRedirect('/adminUser/posts/')
	else:
		context = {'post_form': post_form}
		return render(request,'admin/post_add.html',context)

@login_required
def deletePost(request,num):
    pt = Post.objects.get(postId = num)
    pt.delete()
    return HttpResponseRedirect('/adminUser/posts/') 
@login_required
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
		
@login_required
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
@login_required
def deleteUser(request,num):
	us = ExtendedUser.objects.get(id = num)
	us.delete()
	return HttpResponseRedirect('/adminUser/users/') 

@login_required
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

@login_required
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
@login_required
def isAdmin(request, num):
	us = ExtendedUser.objects.get(id = num)
	us.is_admin = True
	us.is_superuser = True
	us.is_staff = True
	us.save()
	return HttpResponseRedirect('/adminUser/users/') 

@login_required
def blocked(request, num):
	us = ExtendedUser.objects.get(id = num)
	us.is_active = True
	us.save()
	return HttpResponseRedirect('/adminUser/users/')

@login_required
def unblocked(request, num):
	us = ExtendedUser.objects.get(id = num)
	us.is_active = False
	us.save()
	return HttpResponseRedirect('/adminUser/users/')



