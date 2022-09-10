from django.db import models


# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to="products", null=True)
