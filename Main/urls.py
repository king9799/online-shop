"""UzbegimProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Main.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('dashboard/', dashboard, name='dash'),
    path('', log_in, name="login"),
    path('general/', general, name='general'),
    path('table/', table, name='name'),

    path('products_list/', products_list, name='product_list'),
    path('products_add/', products_add, name='product_add'),
    path('products_delete/<int:id>', products_delete, name='products_delete'),
    path('products_edit/<int:id>', products_edit, name='products_edit'),


    path('category_list/', category_list, name='category_list'),
    path('category_add/', category_add, name='category_add'),
    path('category_delete/<int:id>', category_del, name='category_delete'),
    path('category_edit/<int:id>', category_edit, name='category_edit'),

]
