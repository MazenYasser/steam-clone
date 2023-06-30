from django.urls import path, include
from . import views

urlpatterns = [
    path('login', view=views.login, name='login'),
    path('register', view=views.register, name='register'),
]
