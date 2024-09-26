from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category
#a107
from django.contrib.auth.decorators import login_required

from .forms import BlogPostForm, CategoryForm
from django.template.defaultfilters import slugify



#a102
@login_required(login_url='login')
def dashboard(request):
    #a104
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

#a109
def categories(request):
    return render(request, 'dashboard/categories.html')

#a115
def add_category(request):
    #a119
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    #a118
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)


# a121
def edit_category(request, pk):
    #a123
    category = get_object_or_404(Category, pk=pk)
    # a124
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit_category.html', context)

#a126
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

#a128
def posts(request):
    #a130
    #Take from database
    posts = Blog.objects.all()
    context = {
        'posts' : posts,
        
    }
    return render(request, 'dashboard/posts.html', context)

#a134
def add_post(request):
    #a136
    #ngirim ke database
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # temp saving
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
        else:
            pass
    #a135
    #nampilin form post ke FE
    form = BlogPostForm()
    context={
        'form': form
    }
    #mindahin ke url
    return render(request, 'dashboard/add_post.html', context)

#a138
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html', context)


#a140
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')