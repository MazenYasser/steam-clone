from django.shortcuts import render

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'pages/home.html')

def about(request, *args, **kwargs):
    return render(request, 'pages/about.html')

