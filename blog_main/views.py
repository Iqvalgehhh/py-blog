
#a4
from django.shortcuts import render
from blogs.models import Blog, Category
from info.models import About


#a3
def home(request):
    
    #a26
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    #a31
    posts = Blog.objects.filter(is_featured=False, status='Published')
    
    #a69
    #fetch about
    try:
        about = About.objects.get()
    except:
        about = None
    
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)