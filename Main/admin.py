from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Users)
class AdminUser(admin.ModelAdmin):
    list_display = ['user_id', 'first_name', 'phone_number', 'address', 'bonus']
    search_fields = ('user_id', 'first_name', 'phone_number', 'address')


@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
    list_display = ['name_uz', 'name_ru', 'name_en', 'active', 'img']
    search_fields = ('name_uz', 'name_ru', 'name_en')


@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = ['category', 'name_uz', 'name_ru', 'name_en', 'active', 'cr_on']
    search_fields = ('category','name_uz', 'name_ru', 'name_en')


@admin.register(ProductItem)
class AdminProductItem(admin.ModelAdmin):
    list_display = ['product_name', 'name_uz', 'name_ru', 'name_en', 'price', 'amount', 'unit']
    search_fields = ('product_name', 'name_uz', 'name_ru', 'name_en')


@admin.register(Orders)
class AdminOrders(admin.ModelAdmin):
    list_display = ['order_n', 'client', 'summa', 'l_order_item']
    search_fields = ('order_n', 'client')


@admin.register(OrderItem)
class AdminOrders(admin.ModelAdmin):
    list_display = ['order', 'product_item', 'amount', 'summa']
    search_fields = ('order', 'product_item')


@admin.register(Branches)
class AdminBranches(admin.ModelAdmin):
    list_display = ['name_uz', 'address', 'number', 'active']
    search_fields = ('name_uz', 'name_ru', 'name_en')


@admin.register(Extra)
class AdminExtra(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'active']
    search_fields = ('name', 'quantity')


@admin.register(Images)
class AdminExtra(admin.ModelAdmin):
    list_display = ['user', 'image']
    search_fields = ('user',)
