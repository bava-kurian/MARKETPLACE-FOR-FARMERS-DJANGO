from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.CropType)
admin.site.register(models.Farmer)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.Rating)