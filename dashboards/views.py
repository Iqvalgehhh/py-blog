from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category
#a107
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm



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