
#a4
from django.shortcuts import render
from blogs.models import Blog, Category


#a3
def home(request):
    #a26
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    #a31
    posts = Blog.objects.filter(is_featured=False, status='Published')

    context = {
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html', context)