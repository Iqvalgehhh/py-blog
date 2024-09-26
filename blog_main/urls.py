
from django.contrib import admin
from django.urls import include, path
#a2
from . import views
#a17
from django.conf.urls.static import static
from django.conf import settings
#a48
from blogs import views as BlogsView

urlpatterns = [
    path('admin/', admin.site.urls),
    #a1
    path('', views.home, name='home'),
    #a33
    path('category/', include('blogs.urls')),
    #a47
    path('blogs/<slug:slug>/', BlogsView.blogs, name='blogs'),
    #a72
    #search endpoint
    path('blogs/search', BlogsView.search, name='search'),
    #a77
    path('register/', views.register, name='register'),
    # a88
    path('login/', views.login, name='login'),
    # a97
    path('logout/', views.logout, name='logout'),
    #a100
    #dashboard
    path('dashboard/', include('dashboards.urls')),
#a16
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
