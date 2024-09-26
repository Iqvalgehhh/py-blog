#a101
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    #a108
    path('categories/', views.categories, name='categories'),
    #a114
    path('categories/add/', views.add_category, name='add_category'),
    #a120
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    #a125
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
    

]