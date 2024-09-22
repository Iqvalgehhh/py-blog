
from django.contrib import admin
from django.urls import path
#a2
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    #a1
    path("", views.home, name="home")
]
