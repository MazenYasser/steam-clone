from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<game_id>', view=views.checkout, name='checkout'),
    path('success', view=views.paymentSuccess, name='paymentSuccess'),
    path('failed', view=views.paymentFailed, name='paymentFailed')
]

