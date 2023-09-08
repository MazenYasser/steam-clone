
from django import forms
class registerForm(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(max_length=14)        