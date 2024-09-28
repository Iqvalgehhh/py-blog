from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category, Comment
#a74
from django.db.models import Q

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

#a49
def blogs(request, slug):
    #a52
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    # a163
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    # a160
    # comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)

def search(request):
    #a73
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) , status='Published' )
    context = {
        'blogs': blogs,
        #a77
        'keyword': keyword,
    }
    return render(request, 'search.html', context)

