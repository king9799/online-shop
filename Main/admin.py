from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Users)
admin.site.register(Orders)
admin.site.register(OrderItem)
admin.site.register(Products)
admin.site.register(ProductItem)
admin.site.register(Categories)
admin.site.register(Branches)
admin.site.register(Extra)
