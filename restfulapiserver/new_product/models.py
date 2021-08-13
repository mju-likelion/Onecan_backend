from django.db import models
from django.conf import settings

# Create your models here.

class New_product(models.Model):
    product = models.CharField(max_length=100,default="")
    price = models.CharField(max_length=100,default="")
    content = models.TextField()
    image = models.ImageField(default="")

    def __str__(self):
        return self.product