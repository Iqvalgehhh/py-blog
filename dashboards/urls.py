#a101
# nyiapin url 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    #a108
    #category crud
    path('categories/', views.categories, name='categories'),
    #a114
    path('categories/add/', views.add_category, name='add_category'),
    #a120
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    #a125
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
    #a127
    #post crud
    path('posts/', views.posts, name='posts'),
    #a133
    path('posts/add/', views.add_post, name='add_post'),
    #137
    path('posts/edit/<int:pk>/', views.edit_post, name='edit_post'),
    #a139
    path('posts/delete/<int:pk>/', views.delete_post, name='delete_post'),
    # a142
    # users crud
    path('users/', views.users, name='users'),
    # a146
    path('users/add', views.add_user, name='add_user'),
    #a152
    path('users/edit/<int:pk>/', views.edit_user, name='edit_user'),
    #a156
    path('users/delete/<int:pk>/', views.delete_user, name='delete_user'),
    

]