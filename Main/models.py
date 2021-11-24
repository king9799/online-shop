from django.db import models


# Create your models here.
class Users(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()
    address = models.CharField(max_length=200)
    bonus = models.ImageField()
    active = models.DateTimeField(default=True)
    data = models.DateTimeField(auto_created=True)


class Categories(models.Model):
    name_uz = models.CharField(max_length=30)
    name_ru = models.CharField(max_length=30)
    name_en = models.CharField(max_length=30)
    img = models.ImageField()
    active = models.BooleanField(default=True)


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    img = models.ImageField()
    desc_uz = models.TextField(blank=True, null=True)
    desc_ru = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    price = models.ImageField(default=0)
    unit = models.CharField(max_length=20)
    status = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    data = models.DateTimeField(auto_created=True)


class Branches(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    media = models.FileField(blank=True, null=True)
    address = models.CharField(max_length=200)
    number = models.IntegerField(default=0, blank=True, null=True)
    active = models.BooleanField(default=True)


class Extra(models.Model):
    delivery_fee = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0, blank=True, null=True)
    other = models.CharField(max_length=100, blank=True, null=True)



    
