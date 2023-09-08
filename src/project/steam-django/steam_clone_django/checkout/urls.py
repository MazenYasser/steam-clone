from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<game_id>', view=views.checkout, name='checkout'),
    path('paymentSuccess/<game_id>', view=views.paymentSuccess, name='paymentSuccess'),
    path('paymentFailed/<game_id>', view=views.paymentFailed, name='paymentFailed')
]

