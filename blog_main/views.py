
#a4
from django.shortcuts import redirect, render
from blogs.models import Blog, Category
from info.models import About
#a83
from .forms import RegistrationForm
# a93
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


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


#a78
def register(request):
    # a87
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)
    
    
# a89
def login(request):
    # a95
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    # a92
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)
    
    
# a98
def logout(request):
    auth.logout(request)
    return redirect('home')