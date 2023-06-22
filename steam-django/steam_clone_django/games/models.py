from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as lazy
# Create your models here.

def sysreqCheck(requirements : str):
    specs = ["Processor" , "Memory", "OS", "Graphics", "DirectX", "Storage"]
    for spec in specs:
        if requirements.__contains__(spec) == False:
            raise ValidationError(lazy("Must specify all requirements"))

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    gameCount = models.IntegerField() 
    email = models.EmailField(verbose_name="Contact Email")
    
    def __str__(self) -> str:
        return self.name

class Games(models.Model):
    #gameID = models.AutoField(verbose_name= "ID")
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    release_date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)
    requirements = models.TextField(validators=[sysreqCheck])
    price = models.FloatField()
    publisherName = models.ForeignKey(to=Publisher, on_delete=models.DO_NOTHING)
    

    def __str__(self) -> str:
        return self.name