from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default='media/dafault_image.jpeg')

    def __str__(self):
        return self.title
