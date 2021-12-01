from django.db import models


# Create your models here.
class Users(models.Model):
    user_id = models.BigIntegerField(default=0, unique=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    bonus = models.IntegerField(default=0, blank=True, null=True)
    active = models.BooleanField(default=False)
    language = models.CharField(max_length=10, blank=True, null=True)
    data = models.DateTimeField(auto_created=True, blank=True, null=True)
    step = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name


class Categories(models.Model):
    name_uz = models.CharField(max_length=80, blank=True, null=True)
    name_ru = models.CharField(max_length=80, blank=True, null=True)
    name_en = models.CharField(max_length=80, blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_uz


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)
    name_uz = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField()
    desc_uz = models.TextField(blank=True, null=True)
    desc_ru = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    price = models.ImageField(default=0)
    unit = models.CharField(max_length=20)
    status = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    cr_on = models.DateTimeField(auto_created=True, blank=True, null=True)
    cr_up = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name_uz


class Branches(models.Model):
    name_uz = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    desc_uz = models.TextField(blank=True, null=True)
    desc_ru = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)
    media = models.FileField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    number = models.IntegerField(default=0, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_uz


class Extra(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'name:  {self.name} | miqdori: {self.quantity}'

# class Orders(models.Model):
#     client = models.ForeignKey(Users, on_delete=models.CASCADE)
#     desc = models.CharField(max_length=300, blank=True, null=True)
#     time = models.TimeField(auto_now_add=True)
#     order_view = models.ManyToManyField()
#     summa = models.IntegerField(default=0)










    
