
from django.contrib import admin
from django.urls import include, path
#a2
from . import views
#a17
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    #a1
    path("", views.home, name="home"),
    #a33
    path("category/", include('blogs.urls')),

#a16
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
