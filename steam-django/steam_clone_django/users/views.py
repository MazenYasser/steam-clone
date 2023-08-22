from django.shortcuts import render
from .forms import registerForm
from .models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .tokens import account_activation_token, mail_change_token, password_reset_token
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
# Create your views here.

def changeEmail(request, newEmail):
    subject = 'Confirm Email Change'
    message = render_to_string('forms/mailChangeMail.html', {
        'user': request.user.name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(request.user.pk)),
        'newEmail': urlsafe_base64_encode(force_bytes(newEmail)),
        'token': mail_change_token.make_token(request.user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(subject= subject, body= message, to=[request.user.email])
    
    if email.send():  
        messages.success(request, f'Confirmation email sent to {request.user.email}, please go to your current email to confirm email change.\nCheck spam folder.')
    
    else:
        messages.error(request, f'Problem sending email to {request.user.email}, Check if you typed the email correctly and try again.')

def confirmMailChange(request, newEmail, token, uidb64):
    user = get_user_model()
    
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    
    if user is not None and mail_change_token.check_token(user= user, token= token):
        user.email = force_str(urlsafe_base64_decode(newEmail))
        user.save()
        
        messages.success(request, 'Email changed successfully.')
        return render(request, 'forms/accountInfo.html', context={'username': request.user.name , 'phone': request.user.phone, 'email': request.user.email})

def activate(request, uidb64, token):
    user = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user = user, token = token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for activating your account, you can now login.')
        return redirect('users:login')
    else:
        messages.error(request, 'Activation token is invalid.')
    
    return redirect('pages:home')
            
def activationEmail(request, user, to_email):
    subject = 'Activate your account'
    message = render_to_string('forms/activateAccountMail.html', {
        'user': user.name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
        
    })
    email = EmailMessage(subject= subject, body= message, to=[to_email])
    
    if email.send():  
        messages.success(request, f'Activation email sent to {to_email}, please go to the email to activate your account.\nCheck spam folder.')
    
    else:
        messages.error(request, f'Problem sending email to {to_email}, Check if you typed the email correctly and try again.')


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
            user.is_active = False
            activationEmail(request, user, user.email)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
        if username is not None and password is not None and email is not None and phone is not None:  
            return redirect('users:login')
    
    return render(request, 'forms/register.html', {'registerForm' : registerForm})



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, name=username, password=password)
        if user is not None and user.is_active:
            auth_login(request, user)
            return redirect('pages:home')
        elif user is None:
            messages.error(request, 'Invalid username or password')
            return redirect('users:login')
        elif not user.is_active:
            messages.error(request, 'Email is not activated, Please check your email for activation instructions.')
        
    else:
        return render(request, 'forms/login.html' , {})
    
def logout(request):
    auth_logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect("pages:home")

def accountInfo(request):
    if request.method == 'POST' and 'passwordSubmit' in request.POST:
        currentPassword = request.POST.get('currentPassword')
        newPassword = request.POST.get('newPassword')
        match = check_password(currentPassword, request.user.password)
        
        if match:
            newPassword_hashed = make_password(newPassword)
            user = User.objects.get(pk= request.user.id)
            user.password = newPassword_hashed
            user.save()
            messages.success(request, ("Your password has been changed, Please sign in again."))
            return redirect("users:login")
        else:
            messages.error(request, ("Current password is incorrect."))
    elif request.method == "POST" and 'emailSubmit' in request.POST:
        newEmail = request.POST.get('newEmail')
        changeEmail(request, newEmail)
            
    return render(request, 'forms/accountInfo.html', context={'username': request.user.name , 'phone': request.user.phone, 'email': request.user.email})

def forgotPassword(request):
    user = get_user_model()
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            
        except(User.DoesNotExist, TypeError, OverflowError):
            user = None
        
        if user is not None:
            to_email = user.email
            passwordResetMail(request, user, to_email)
                
    return render(request, 'forms/forgotPassword.html')

def passwordResetMail(request, user, to_email):    
    subject = "Reset your password"
    message = render_to_string('forms/forgotPasswordMail.html', context={
        'user': user.name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': password_reset_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
        
    })
    
    email = EmailMessage(subject= subject, body= message, to=[to_email])
    
    if email.send():  
        messages.success(request, f'An email was sent to {to_email}, please go to the email to reset your password.\nCheck spam folder.')
    
    else:
        messages.error(request, f'Problem sending email to {to_email}, Check if you typed the email correctly and try again.')

def passwordReset(request, uidb64, token):
    user = get_user_model()
    
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and password_reset_token.check_token(user = user, token = token):
        if request.method == "POST":
            newPassword = request.POST.get("newPassword")
            newPasswordConfirm = request.POST.get("newPasswordConfirm")
            
            if newPassword != newPasswordConfirm:
                messages.error(request, "Passwords do not match")
                
            elif newPassword == newPasswordConfirm:
                newPassword_hashed = make_password(newPassword)
                user.password = newPassword_hashed
                user.save()
                messages.success(request, "Password has been changed successfully, please sign in again")
                return redirect("users:login")
    
    return render(request, 'forms/passwordReset.html')
