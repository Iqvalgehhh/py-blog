from django.contrib import admin
from django.http import HttpRequest
from .models import Category, Blog

#a22
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    #a23
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)

#a12
admin.site.register(Category)
#a21
admin.site.register(Blog, BlogAdmin)


