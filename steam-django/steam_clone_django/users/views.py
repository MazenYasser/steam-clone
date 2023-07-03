from django.shortcuts import render
from .forms import registerForm
from .models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        form = registerForm({'name': username, 'password': password , 'email': email, 'phone': phone})
        hashed_psw = make_password(password)
        
        if form.is_valid():
            user = User(name= username, password=hashed_psw, email=email, phone=phone)
            user.save()
        if username is not None and password is not None and email is not None and phone is not None:  
            return redirect('login')
    
    return render(request, 'forms/register.html', {'registerForm' : registerForm})



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, name=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('../pages/home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
        
    else:
        return render(request, 'forms/login.html' , {})
    
def logout(request):
    auth_logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect("../pages/home")