from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from post import views
# from .views import post,category, category_detail

urlpatterns = [    
	path('post/<post_id>/', views.post,name='post'),
	path('category/', views.category,name='category'),
	path('list/<cat_id>', views.category_detail,name='list'),
    ]
