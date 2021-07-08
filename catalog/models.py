from typing import Any
from django.db import models

# Create your models here.


class Category(models.Model):
    description = models.CharField(max_length=100, verbose_name="Descripción")

    def __str__(self):
        return self.description


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    image = models.ImageField(upload_to='catalog/')
    description = models.TextField(verbose_name="Descripción")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=11)
    stock = models.IntegerField(verbose_name="Stock", default=0)

    def __str__(self):
        return self.title
