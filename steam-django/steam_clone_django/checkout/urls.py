from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<game_id>', view=views.checkout, name='checkout'),
    path('paymentSuccess', view=views.paymentSuccess, name='paymentSuccess'),
    path('paymentFailed', view=views.paymentFailed, name='paymentFailed')
]

