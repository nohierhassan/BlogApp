from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.


class Category(models.Model):
    categoryId   = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=30)
    userId       = models.ManyToManyField(settings.AUTH_USER_MODEL,blank = True)
    def __str__(self):
        return self.categoryName

# class UserModel(AbstractUser):
#     user=models.ManyToManyField(Category)
 

class Tag(models.Model):
    tagId=models.AutoField(primary_key=True)
    tagName=models.CharField(max_length=50)
    def __str__(self):
        return self.tagName


#def upload_location(instance, filename):
    #file_path = 'blog/{author_id}/{postTitle}-{filename}'.format(
                #author_id=str(instance.postAuthor .id),postTitle=str(instance.postTitle), filename=filename)
    #return file_path
class Post(models.Model):
    postId                      = models.AutoField(primary_key=True)
    postTitle                   = models.CharField(max_length=50, null=False, blank=False)
    postBody                    = models.TextField(max_length=500, null=False, blank=False)
    postImage                   = models.ImageField(upload_to="media/", null=True, blank=True)
    postDatePublished           = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    postDateUpdated             = models.DateTimeField(auto_now=True, verbose_name="date updated")
    postAuthor                  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    postCategory                = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
   # postSlug                    = models.SlugField(blank=True, unique=True)
    postTag                     = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.postTitle
        

class Comment(models.Model):
    commentId    = models.AutoField(primary_key=True)
    postId       = models.ForeignKey(Post,on_delete=models.DO_NOTHING)
    commentContent      = models.CharField(max_length=150)
    commentDate         = models.DateTimeField(auto_now=True, auto_now_add=False)
    commentAuthor       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        ordering = ['commentDate']
    def __str__(self):
        return 'Comment {}'.format(self.body)

class ForbiddenWord(models.Model):
    wordId=models.IntegerField(primary_key=True)
    word=models.CharField(max_length=20)
    def __str__(self):
        return self.word


