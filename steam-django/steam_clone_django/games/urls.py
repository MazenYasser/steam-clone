from django.urls import path
from . import views

urlpatterns = [
    path('gameTemplate/<game_id>', view=views.game, name='game'),
]

