from django.shortcuts import render
from .models import Games
# Create your views here.

def mk11(request):
    return render(request, 'games/mk11.html', context= {"game" : Games.objects.get(name = "Mortal Kombat 11")} )

def csgo(request):
    return render(request, 'games/csgo.html')