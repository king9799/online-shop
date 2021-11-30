from django.db import models

# Create your models here.
class Bot_User(models.Model):
    user_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_img = models.ImageField(blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
