from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Publisher)
admin.site.register(models.Games)
admin.site.register(models.Review)