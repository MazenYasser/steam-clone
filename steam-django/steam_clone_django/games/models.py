from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as lazy
# Create your models here.

def sysreqCheck(requirements : str):
    specs = ["Processor" , "Memory", "OS", "Graphics", "DirectX", "Storage"]
    for spec in specs:
        if requirements.__contains__(spec) == False:
            raise ValidationError(lazy("Missing requirement: " + spec))

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
    img_cover = models.ImageField(verbose_name='Splash Art',upload_to='photos/%y/%m/%d', height_field=None, width_field=None, max_length=None, default=None, null=True, blank=True)
    img_1 = models.ImageField(verbose_name='Trailer Image 1',upload_to='photos/%y/%m/%d', height_field=None, width_field=None, max_length=None, default=None, null=True, blank=True)
    img_2 = models.ImageField(verbose_name='Trailer Image 2',upload_to='photos/%y/%m/%d', height_field=None, width_field=None, max_length=None, default=None, null=True, blank=True)
    img_3 = models.ImageField(verbose_name='Trailer Image 3',upload_to='photos/%y/%m/%d', height_field=None, width_field=None, max_length=None, default=None, null=True, blank=True)
    trailer = models.FileField(verbose_name='Video Trailer',upload_to='videos/%y/%m/%d', blank=True, null=True)
    developerName = models.CharField(max_length=50)
    publisherName = models.ForeignKey(to=Publisher, on_delete=models.DO_NOTHING)
    

    def __str__(self) -> str:
        return self.name