from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime
from category.models import Category

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    quantity=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)

    def __str__(self):
            return self.name