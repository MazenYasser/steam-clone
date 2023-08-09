from django.urls import path, include
from . import views

urlpatterns = [
    path('', view=views.login, name='login'),
    path('register', view=views.register, name='register'),
    path('logout', view=views.logout, name='logout'),
    path('activate/<uidb64>/<token>', view=views.activate, name='activate'),
    path('accountInfo', view=views.accountInfo, name='accountInfo'),
    path('confirmMailChange/<uidb64>/<token>/<newEmail>', view=views.confirmMailChange, name='confirmMailChange'),
    path('forgotPassword', view=views.forgotPassword, name='forgotPassword'),
    path('passwordReset/<uidb64>/<token>', view=views.passwordReset, name='passwordReset'),
]
