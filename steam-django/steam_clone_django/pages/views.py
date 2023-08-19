from django.shortcuts import render
from games.models import Games
# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'pages/home.html', context= {'games': Games.objects.all() , 'n': range(1,4)})

def about(request, *args, **kwargs):
    return render(request, 'pages/about.html')

def search(request):
    if request.method == 'GET':
        searched_game = request.GET.get('searched')
        games = Games.objects.filter(name__icontains = searched_game)
        categories = Games.objects.values_list('category', flat=True).distinct()
    return render(request, 'pages/searchResult.html', context={'searched': searched_game , 'games': games , 'categories': categories})

def searchByCategory(request):
    if request.method == 'GET':
        searched_game = request.GET.get('searched')
        category = request.GET.get('category')
        if category is not None:
            categories = Games.objects.values_list('category', flat=True).distinct()
            filtered_games = Games.objects.filter(category = category)
        else:
            return search(request)
            
    return render(request, 'pages/searchResult.html', context={'searched': searched_game, 'games': filtered_games, 'categories': categories})