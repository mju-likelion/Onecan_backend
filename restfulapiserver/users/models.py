from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
