from django.shortcuts import render
from games.models import Games
# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'pages/home.html', context= {'games': Games.objects.all()})

def about(request, *args, **kwargs):
    return render(request, 'pages/about.html')

