from django.shortcuts import render
from games.models import Games
# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'pages/home.html', context= {'games': Games.objects.all() , 'n': range(1,4)})

def about(request, *args, **kwargs):
    return render(request, 'pages/about.html')

def search(request):
    if request.method == 'POST':
        searched_game = request.POST.get('searched')
        games = Games.objects.filter(name__contains = searched_game)
    return render(request, 'pages/searchResult.html', context={'searched': searched_game , 'games': games})