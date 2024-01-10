from django.db import models

class Stock(models.TextChoices):
    si = 'si'
    no = 'no'

class Producto(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=30)
    precio=models.IntegerField(default='0')
    stock=models.CharField(max_length=3, choices=Stock)

