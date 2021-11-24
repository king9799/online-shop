from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()
    address = models.CharField(max_length=200)
    bonus = models.ImageField()
    active = models.DateTimeField(default=True)


class Category(models.Model):
    name_uz = models.CharField(max_length=30)
    name_ru = models.CharField(max_length=30)
    name_en = models.CharField(max_length=30)
    img = models.ImageField()
    active = models.BooleanField(default=True)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    img = models.ImageField()
    desc_uz = models.TextField()
    desc_ru = models.TextField()
    desc_en = models.TextField()
    price = models.ImageField(default=0)
    unit = models.CharField(max_length=20)
    status = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)




