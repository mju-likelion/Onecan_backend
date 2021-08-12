from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class User(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20)
    password1 = models.CharField(max_length=20)
    # password2 = models.CharField(max_length=20)


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    # photo = models.ImageField(upload_to= 'photo')

    def __str__(self):
        return self.product_name


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=20)
    recipe_description = models.TextField()

    def __str__(self):
        return self.recipe_name


class Barter(models.Model):
    barter_name = models.CharField(max_length=20)
    barter_description = models.TextField()

    def __str__(self):
        return self.barter_name

