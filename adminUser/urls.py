from django.urls import path
from adminUser import views
urlpatterns = [
    path('home/', views.home,name = "adminhome"),
    path('users/', views.users),
    path('posts/', views.posts),
    path('categories/', views.categories),
    path('forbiddenwords/', views.forbiddenWords),
    path('forbiddenwords/editWord/<num>',views.editWord),
    path('forbiddenwords/deleteWord/<num>',views.deleteWord),
    path('forbiddenwords/addWord',views.addWord),
    path('categories/editCategory/<num>',views.editCategory),
    path('categories/deleteCategory/<num>',views.deleteCategory),
    path('categories/addCategory',views.addCategory),
    path('posts/editPost/<num>',views.editPost),
    path('posts/deletePost/<num>',views.deletePost),
    path('posts/addPost',views.addPost),
    path('users/addUser',views.addUser),
    path('users/deleteUser/<num>',views.deleteUser),
    path('users/editUser/<num>',views.editUser),
    path('posts/addTag',views.addTag),
    path('users/isAdmin/<num>',views.isAdmin),
    path('users/blocked/<num>',views.blocked),
    path('users/unblocked/<num>',views.unblocked),




]