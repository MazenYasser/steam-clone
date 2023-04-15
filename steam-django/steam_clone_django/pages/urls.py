from django.urls import path
from . import views

urlpatterns = [
    path('home', view=views.home, name='home'),
    path('about', view=views.about, name='about')
]

