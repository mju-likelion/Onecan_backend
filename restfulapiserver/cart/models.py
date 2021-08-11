from django.db import models
from django.conf import settings


    # product_name = models.CharField(max_length=30)
    # price = models.CharField(max_length=30)

    # photo = models.ImageField(upload_to="image")




class Cart(models.Model):
    TYPE_CHOICES =  [('1','1'),('2','2'),('3','3'),('4','4'),]
    product = models.CharField(max_length=100)
    price = models.TextField()
    content = models.TextField()
    

