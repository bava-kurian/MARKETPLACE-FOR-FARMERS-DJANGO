from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class CropType(models.Model):
    
    name=models.CharField(max_length=255, unique=True)
    
    
    def __str__(self):
        return self.name;
    
class Farmer(models.Model):
    
    user=models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    crops=models.ManyToManyField(CropType)
    
    def __str__(self):
        return self.user.username
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
class Rating(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    value=models.IntegerField();
    
    def __str__(self):
        return self.product.name,self.value
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'