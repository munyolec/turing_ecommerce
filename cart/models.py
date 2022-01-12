from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime


# Create your models here.

class Cart(models.Model):
     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
     quantity = models.PositiveIntegerField(default=0)
     total_price = models.DecimalField(decimal_places=2,max_digits=10, default=0.00)
     updated = models.DateTimeField(auto_now=True)
     timestamp = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return "User: {} has {} items in their cart. Their total is ${}".format(self.user, self.count, self.total)
    

class Entry(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, null= True, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return "This entry contains {} {}(s).".format(self.quantity, self.product.name)