from django.shortcuts import render
from .models import Games
# Create your views here.

def game(request, game_id):
    req_game = Games.objects.get(pk=game_id)
    return render(request, 'games/gameTemplate.html', context= {"game" : req_game})

def csgo(request):
    return render(request, 'games/csgo.html')