from BlogApp.models import *
from django import forms

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
        fields = ('categoryName',)
        widgets = {
                    'categoryName' : forms.TextInput( attrs={'class': 'form-control '}),
                    }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('postTitle','postBody','postAuthor','postCategory','postImage','postTag','postSlug')
        widgets = {
                    'postTitle' : forms.TextInput( attrs={'class': 'form-control '}),
                    'postBody': forms.Textarea( attrs={'class': 'form-control '}),
                    'postAuthor': forms.Select( attrs={'class': 'form-control '}),
                    'postCategory': forms.Select( attrs={'class': 'form-control '}),
                    'postImage': forms.FileInput( attrs={'class': 'form-control '}),
                    'postTag': forms.TextInput( attrs={'class': 'form-control '}),
                    'postSlug': forms.TextInput( attrs={'class': 'form-control '}),

                    }


