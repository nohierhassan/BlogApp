# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from BlogApp.models import Post,Category,Tag,Comment
# from .forms import CommentForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login as authlogin

def category(request):
	category=Post.objects.all()
	context={'category':category}
	return render (request,'post/category.html',context)

def post(request, post_id):
	all_categories= Category.objects.all()
	post=get_object_or_404(Post,pk=post_id)
	all_Tags= Tag.objects.all()
	# comments = Comment.objects.filter(postId=post.postId)
	# new_comment = None

	# if request.method == 'POST':
	# 	comment_form = CommentForm(data=request.POST)
	# 	if comment_form.is_valid():

			
	# 		new_comment = comment_form.save(commit=False)
	# 		new_comment.commentAuthor=request.user
	# 		new_comment.post = post

	# 		new_comment.save()
	# else:
	# 	comment_form = CommentForm()


	context={
	'post':post,
	'all_categories':all_categories,
	'all_Tags':all_Tags,
	'category':category,
	# 'comments': comments,
	# 'new_comment': new_comment,
	# 'comment_form': comment_form
	}
	return render (request,'post/post.html',context)

def category_detail(request, cat_id):
    category = get_object_or_404(Category,pk=cat_id)
    post= Post.objects.filter(postCategory=cat_id)
    return render(request,'post/list.html', {
        'category': category,
        'post':post,
    })






