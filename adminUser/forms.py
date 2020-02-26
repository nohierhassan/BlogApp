from BlogApp.models import *
from django import forms
from AccountsApp.models import ExtendedUser

class WordForm(forms.ModelForm):
    class Meta:
        model = ForbiddenWord
        fields = ('word',)
        widgets = {
                    'word' : forms.TextInput( attrs={'class': 'form-control '}),
                    }
                    

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('categoryName','userId')
        widgets = {
                    'categoryName' : forms.TextInput( attrs={'class': 'form-control '}),
                    }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('postTitle','postBody','postCategory','postImage','postTag')
        widgets = {
                    'postTitle' : forms.TextInput( attrs={'class': 'form-control '}),
                    'postBody': forms.Textarea( attrs={'class': 'form-control '}),
                    'postCategory': forms.Select( attrs={'class': 'form-control '}),
                    'postImage': forms.ClearableFileInput( attrs={'class': 'form-control '}),
                    'postTag': forms.CheckboxSelectMultiple( attrs={'class': 'form-control '}),

                    }


class UserForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ('username','password','email')
        widgets = {
                    'username' : forms.TextInput( attrs={'class': 'form-control '}),
                    'password' : forms.PasswordInput( attrs={'class': 'form-control '}),
                    'email' : forms.EmailInput( attrs={'class': 'form-control '}),

                    }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('tagName',)
        widgets = {
                    'tagName' : forms.TextInput( attrs={'class': 'form-control '}),
                    }


class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commentContent',)

