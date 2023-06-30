from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)
    spendings = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.username
    