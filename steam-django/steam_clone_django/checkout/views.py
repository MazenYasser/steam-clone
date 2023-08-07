from django.shortcuts import render
from django.http import HttpResponse
from games.models import Games
from checkout.models import Order
from users.models import User
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from random import randrange
# Create your views here.

@login_required
def checkout(request, game_id):
    req_game = Games.objects.get(pk=game_id)
    if Order.objects.filter(user_id = request.user, game = req_game).exists():
        isOwned = True
        return render(request, 'checkoutForms/checkout.html', {'game': req_game,'isOwned': isOwned})
    
    if (Order.objects.count() != 0):
        invoice_id = Order.objects.latest('id')
        invoice_id = invoice_id.id + 100
    else:
        invoice_id = randrange(100,1000)
    
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(req_game.price),
        'item_name': str(req_game.name),
        'invoice': 'INVOICE-NO-{}'.format(invoice_id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('checkout:paymentSuccess', kwargs= {'game_id': game_id})),
        'cancel_url': 'http://{}{}'.format(host, reverse('checkout:paymentFailed', kwargs= {'game_id': game_id}))
    }
    
    paypal_payment_button = PayPalPaymentsForm(initial = paypal_dict)
    
    return render(request, 'checkoutForms/checkout.html', {'game': req_game, 'paypal_payment_button': paypal_payment_button})

def paymentSuccess(request, game_id):
    req_game = Games.objects.get(pk=game_id)
    newOrder = Order(user_id = request.user, game = req_game, cost = req_game.price)
    newOrder.save()
    send_mail(subject="Your game purchase was successfull", message=f"Thank you {request.user.name} for your purchase of {req_game.name}.\nWe hope you will enjoy it."
              , fail_silently= False, from_email="settings.EMAIL_HOST_USER", recipient_list=[User.objects.get(pk=request.user.id).email])
    return render(request, 'checkoutForms/paymentSuccess.html')

def paymentFailed(request, game_id):
    return render(request, 'checkoutForms/paymentFailed.html')