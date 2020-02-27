from BlogApp.models import Comment
from django.db import models
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commentContent',)

 