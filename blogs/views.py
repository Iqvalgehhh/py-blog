from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category

#a35
def posts_by_category(request, category_id):
    #a36
    #fetch posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    #a38
    #use try/except when want to do some custom action incase category does not exist
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     #redirect to homepage
    #     return redirect('home')
    #use get_object_or_404 when want to show 404 error page incase category doesn't exist
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category' : category,
    }
    return render(request, 'posts_by_category.html', context)
