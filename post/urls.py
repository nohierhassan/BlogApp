from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from post import views
# from .views import post,category, category_detail

urlpatterns = [    
	path('post/<post_id>/', views.post,name='post'),
	path('category/', views.category,name='category'),
	path('list/<cat_id>', views.category_detail,name='list'),

	path('post/like/<post_id>',views.like)
	# path('post/like/<num>/',views.like,name='like'),
	# path('post/notlike/<num>/',views.notlike,name='notlike'),
	# path('post/dislike/<num>/',views.dislike,name='dislike'),
	# path('post/notdislike/<num>/',views.notdislike,name='notdislike'),
]
