from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime


# Create your models here.


class Cart(models.Model):
     user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)    
     total_price = models.DecimalField(decimal_places=2,max_digits=10, default=0.00)
     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
     def __str__(self):
         return str(self.id)

class Entry(models.Model):
    product = models.CharField(max_length=255, default='none')
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    product_price=models.DecimalField(decimal_places=2,max_digits=10, default=0.00)
    quantity = models.PositiveIntegerField()
    total_price=models.DecimalField(decimal_places=2,max_digits=10, default=0.00)
    cart = models.ForeignKey(Cart,null=True, blank=True, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "This entry contains {} {}(s).".format(self.quantity, self.product)


            