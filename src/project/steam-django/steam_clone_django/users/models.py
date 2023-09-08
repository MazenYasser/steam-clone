from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, phone, **extra_fields):
        if not name:
            raise ValueError('Invalid name')
        if not email:
            raise ValueError('Invalid email')
        email = self.normalize_email(email)
        user = self.model(email = email, name = name, phone = phone, **extra_fields)
        user.set_password(password)
        user.save(using= self.db)
        return user
    
    def create_user(self, name = None, email = None, password = None, phone = None, **extra_fields):
        extra_fields.setdefault('is_superuser', False) # NAME MUST BE EXACTLY AS USED
        extra_fields.setdefault('is_staff', False) # NAME MUST BE EXACTLY AS USED
        extra_fields.setdefault('spendings', 0)

        return self._create_user(name=name, email=email, password=password, phone= phone, **extra_fields)
        
    def create_superuser(self, name = None, email = None, password = None, phone = None ,**extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        
        return self._create_user(name=name, email=email, password=password, phone = phone, **extra_fields)
        
        
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, unique=True) # NAME MUST BE EXACTLY AS USED, This field must exist and in the same name
    password = models.CharField(max_length=500, unique=True)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=254, blank=True, default='')
    spendings = models.PositiveIntegerField(blank=True, null=True)
    
    # For user management (superuser and staff must exist)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    dateJoined = models.DateTimeField(default=timezone.now)
    lastLogin = models.DateTimeField(blank=True, null=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'name'
    EMAIL_FIELD = 'email'
    
    REQUIRED_FIELDS = ['phone', 'email']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]    
    
    def __str__(self):
        return self.name
    