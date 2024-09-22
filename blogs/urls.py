from django.urls import  path
from . import views


#a34
urlpatterns = [
path('<int:category_id>/', views.posts_by_category, name='posts_by_category')
]