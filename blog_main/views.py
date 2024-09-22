
#a4
from django.shortcuts import render


#a3
def home(request):
    return render(request, 'home.html')