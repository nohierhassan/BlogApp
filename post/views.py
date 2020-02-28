# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.

# from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from BlogApp.models import Post,Category,Tag,Comment,Likes
from AccountsApp.models import ExtendedUser
from django.conf import settings
from .forms import *
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
    post=get_object_or_404(Post,pk=post_id)
    all_Tags= Tag.objects.all()
    is_liked=None
    like = Likes.objects.filter(post_id=post.postId)
    post_likes = like.filter(like = True).count()
    post_dislikes = like.filter(like = False).count()
    if request.user.is_authenticated:
        like = Likes.objects.filter(post_id=post, userId=request.user.id)

        if like.exists():
            if like.get().like == True:
                is_liked=True
            else:
                is_liked=False

    comments=Comment.objects.filter(postId=post.postId , reply=None)
    if request.method =='POST':
        comment_form=CommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('commentContent')
            reply_id=request.POST.get('comment_id')
            comment_qs=None
            if reply_id:
                comment_qs=Comment.objects.get(commentId=reply_id)
            comment=Comment.objects.create(postId=post,commentAuthor=request.user , commentContent=content , reply=comment_qs)
            comment.save()
            comment_form = CommentForm()

    else : 
        comment_form=CommentForm()  

    context={
    'post':post,
    'all_categories':all_categories,
    'all_Tags':all_Tags,
    'category':category,
    'comments': comments,
    'is_liked': is_liked, 
    'post_likes': post_likes, 
    'post_dislikes': post_dislikes,
    'comment_form': comment_form,



    }
    return render (request,'post/post.html',context)


def category_detail(request, cat_id):
    category = get_object_or_404(Category,pk=cat_id)
    post= Post.objects.filter(postCategory=cat_id).order_by('-postDatePublished')
    return render(request,'post/list.html', {
        'category': category,
        'post':post,
    })

def like(request,post_id):

    if not Likes.objects.filter(post_id=post_id, userId=request.user.id).exists():
        post = Post.objects.get(postId=post_id)

        if request.POST.get('like') == '1':
            Likes.objects.create(post_id=post, userId=request.user, like = True)
        else:
            Likes.objects.create(post_id=post, userId=request.user, like = False)

        dislike = Likes.objects.filter(post_id=post, like = False)
        if dislike.count() >= 10:
            # dislike.delete()
            post.delete()

            return HttpResponseRedirect('/blog/home/')

    return HttpResponseRedirect('/post/post/' + post_id)

