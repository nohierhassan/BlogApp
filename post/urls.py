from django.contrib import admin
from django.urls import path,include
from post import views

urlpatterns = [    
	path('post/<int:post_id>/', views.post,name='post'),
	path('category/', views.category,name='category'),
    ]
