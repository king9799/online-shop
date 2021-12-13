from .models import *


def get_category():
    return Categories.objects.all()


def get_product(cat_id):
    return Products.objects.filter(category=cat_id)


def get_product_item(pro_id):
    return ProductItem.objects.filter(product_name=pro_id)


def get_order(client_id):
    return Orders.objects.get(client_id=client_id)


def get_order_item():
    return OrderItem.objects.all()