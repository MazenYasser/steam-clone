from django.urls import path
from . import views

urlpatterns = [
    path('home', view=views.home, name='home'),
    path('about', view=views.about, name='about'),
    path('search', view=views.search, name='search'),
    path('searchByCategory', view=views.searchByCategory, name='searchByCategory'),
]

