from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class Category(models.Model):
#     categoryId = models.IntegerField(primary_key=True)
#     name=models.CharField(max_length=30)

# class UserModel(AbstractUser):
#     user=models.ManyToManyField(Category)


# class Tag(models.Model):
#     tagId=models.IntegerField(primary_key=True)
#     tagname=models.CharField(max_length=50)



class Post(models.Model):
    postId=models.AutoField(primary_key=True)
    title=models.CharField(max_length=30)
    content=models.CharField(max_length=300)
    date=models.DateField(("Default"), auto_now=True, auto_now_add=False)
    #id=models.ForeignKey(UserModel,on_delete=models.DO_NOTHING)
    #categoryId=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    image=models.ImageField(("Default"), upload_to=None, height_field=None, width_field=None, max_length=None)
    def __str__(self):
      return self.title
  #  tags=models.ManyToManyField(Tag)


# class Comment(models.Model):
#     commentId=models.IntegerField(primary_key=True)
#     postId=models.ForeignKey(Post,on_delete=models.DO_NOTHING)
#     content=models.CharField(max_length=150)
#     date=models.DateTimeField(("Default"), auto_now=True, auto_now_add=False)

# class ForbiddenWord(models.Model):
#     fId=models.IntegerField(primary_key=True)
#     word=models.CharField(max_length=20)



# class tagPost(models.Model):
#     postId=models.ForeignKey(postId)
#     tagId=models.ForeignKey(postId)

# class categoryUser(models.Model):
#     categoryId=models.ForeignKey(categoryId)
#     Id=models.ForeignKey(User)

    


