# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.

# from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from BlogApp.models import Post,Category,Tag,Comment,Likes
from .forms import CommentForm
from AccountsApp.models import ExtendedUser
from django.conf import settings
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login as authlogin
User = settings.AUTH_USER_MODEL
def category(request):
	category=Post.objects.all()
	context={'category':category}
	return render (request,'post/category.html',context)

def post(request, post_id):
	all_categories= Category.objects.all()
	post=Post.objects.get(postId = post_id)
	all_Tags= Tag.objects.all()
	comments = Comment.objects.filter(postId=post.postId)
	total_likes= Likes.objects.filter(postId=post_id).filter(likes=True).count()
	total_dislikes= Likes.objects.filter(postId=post_id).filter(likes=False).count()
	likes=Likes.objects.get(postId=post_id)
	new_comment = None

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():		
			new_comment = comment_form.save(commit=False)
			new_comment.commentAuthor = request.user 
			new_comment.postId = post  
			new_comment.save()
	else:
		comment_form = CommentForm()


	context={
	'post':post,
	'all_categories':all_categories,
	'all_Tags':all_Tags,
	'category':category,
	'comments': comments,
	'new_comment': new_comment,
	'comment_form': comment_form,
	'total_likes':total_likes,
	'total_dislikes':total_dislikes,
	'likes':likes
	}
	return render (request,'post/post.html',context)

def category_detail(request, cat_id):
    category = get_object_or_404(Category,pk=cat_id)
    post= Post.objects.filter(postCategory=cat_id).order_by('-postDatePublished')
    return render(request,'post/list.html', {
        'category': category,
        'post':post,
    })






def like(request,num):
	post=get_object_or_404(Post,pk=num)
	user=request.user
	like=Likes(pId=post,User=user,likes = True)
	like.save()


	return HttpResponseRedirect("post/post/num")



def notlike(request,num):
	like=Likes.objects.get(pId=num)
	like.delete()
	return HttpResponseRedirect("post/post/num")


def dislike(request,num):
	post=get_object_or_404(Post,pk=num)
	user=request.user
	dislike=Likes(pId=post,User=user,likes = False)
	dislike.save()
	return HttpResponseRedirect("post/post/num")


def notdislike(request,num):
	dislike=Likes.objects.get(pId=num)
	dislike.delete()
	return HttpResponseRedirect("post/post/num")