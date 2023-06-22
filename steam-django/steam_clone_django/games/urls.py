from django.urls import path
from . import views

urlpatterns = [
    path('mk11', view=views.mk11, name='mk11'),
    path('csgo', view=views.csgo, name='csgo')
]

