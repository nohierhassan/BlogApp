from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Category(models.Model):
	categoryId = models.IntegerField(primary_key=True)
    name=models.CharField()

class Post(models.Model):
    postId=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=30)
    content=models.charField()
    date=models.DateField(_(""), auto_now=True, auto_now_add=False)
    userId=models.ForeignKey(userId)
    categoryId=models.ForeignKey(categoryId)
    image=models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    
class Tag(models.Model):
    tagId=models.IntegerField(primary_key=True)
    tagname

class Comment(models.Model):
    commentId=models.IntegerField(primary_key=True)
    postId=models.ForeignKey(postId)
    content=models.CharField()
    date=models.DateField(_(""), auto_now=True, auto_now_add=False)

# class ForbiddenWord(models.Model):
#     fId=models.IntegerField(primary_key=True)
#     word=models.CharField()

class Users(AbstractUser):
    isAdmin=models.Boolea­nField()
    isBlocked=models.BooleanField()



class tagPost(models.Model):
    postId=models.ForeignKey(postId)
    tagId=models.ForeignKey(postId)

class categoryUser(models.Model):
    categoryId=models.ForeignKey(categoryId)
    userId=models.ForeignKey(userId)

    


