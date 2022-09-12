from django.db import models


# Create your models here.


class Tax(models.Model):
    name = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}({self.id})'


class Discount(models.Model):
    name = models.CharField(max_length=100)
    coupon_id = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}({self.id})'


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to="products", null=True)
    taxes = models.ManyToManyField(Tax)

    def __str__(self):
        return f'{self.name}({self.id})'


class Order(models.Model):
    details = models.JSONField()
    status = models.CharField(max_length=50, choices=[
        ('P', 'Pending'),
        ('S', 'Successful')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
