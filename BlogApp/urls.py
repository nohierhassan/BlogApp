
from django.contrib import admin
from django.urls import path,include
from BlogApp import views

urlpatterns = [		

	path('home/', views.home,name='home'),
    path('post/<int:post_id>/', views.post,name='post'),
	
    path('category/', views.category,name='category'),
	
    path('register/', views.register,name = 'register'),	
    
    path('login/', views.login),	
    
    path('home/search/',views.search),
    
    path('post/post/<num>',views.showpost),


    path('home/<numb>',views.subscribe),  
    #path('home/sub/',views.subscribe),
    # path('register/', views.register,name = 'register'),	
    #path('login/', views.login),	

	path('blocked/', views.blocked,name="blocked"),
]
