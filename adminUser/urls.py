from django.urls import path
from adminUser import views
urlpatterns = [
    path('home/', views.home),
    path('users/', views.users),
    path('posts/', views.posts),
    path('categories/', views.categories),
    path('forbiddenwords/', views.forbiddenWords) 	 		
]