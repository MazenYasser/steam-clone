from django.shortcuts import render
from django.http import HttpResponse
from games.models import Games
from checkout.models import Order
from users.models import User
# Create your views here.
def checkout(request, game_id):
    req_game = Games.objects.get(pk=game_id)
    newOrder = Order(user_id = request.user, game = req_game, cost = req_game.price)
    newOrder.save()
    return render(request, 'checkoutForms/checkout.html', {'game': req_game})

def paymentSuccess(request):
    return render(request, 'checkoutForms/paymentSuccess.html')

def paymentFailed(request):
    return render(request, 'checkoutForms/paymentFailed.html')