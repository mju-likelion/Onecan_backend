from django.db import models
from django.conf import settings


class Barter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default="")

    def __str__(self):
        return self.title
