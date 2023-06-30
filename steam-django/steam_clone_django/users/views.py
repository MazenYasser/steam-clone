from django.shortcuts import render
from .forms import registerForm
from .models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        form = registerForm({'username': username, 'password': password , 'email': email, 'phone': phone})
        if form.is_valid():
            user = User(username= username, password=password, email=email, phone=phone)
        if username != None and password != None and email != None and phone != None:  
            user.save()
    
    return render(request, 'forms/register.html', {'registerForm' : registerForm})



def login(request):
    return render(request, 'forms/login.html')