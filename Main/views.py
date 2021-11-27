from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *


# Create your views here.

def index(request):
    return render(request, "index.html")


def dashboard(request):
    return render(request, 'dashboard.html')


def log_in(request):
    print(request.POST)
    if request.method == "POST":
        # print(request.POST)
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(
        #     request,
        #     username=username,
        #     password=password,
        # )
        # if user is None:
        #     return redirect("/")
        # login(request, user)
        return redirect('/dashboard')
    else:
        return render(request, 'login.html')


def general(request):
    return render(request, 'general.html')


def category_list(request):
    category = Categories.objects.all()
    return render(request, 'category/category_list.html', {'categories': category})


def category_add(request):
    if request.method == "POST":
        print(request.POST)
        a = request.POST
        cat = Categories.objects.create(

            name_uz=a['name_uz'],
            name_ru=a['name_ru'],
            name_en=a['name_en'],
            img=a['img']
        )
        cat.save()
        return redirect('/category_list')
    return render(request, 'category/category_add.html')


def category_edit(request, id):
    category = Categories.objects.get(id=id)
    categories = Categories.objects.all()
    if request.method == 'POST':
        a = request.POST
        categories.name = a["name_uz"]
        categories.save()
        return redirect('/dashboard')
    return render(request, "category/category_edit.html", {'category': category, 'categories': categories})


def category_del(request, id):
    category = Categories.objects.get(id=id)
    category.delete()
    return redirect('/category_list')


def table(request):
    return render(request, 'data.html')


def products_list(request):
    products = Products.objects.all()
    return render(request, 'products/products_list.html', {'products': products})


def products_add(request):
    print(request.POST)
    if request.method == "POST":
        a = request.POST
        product = Products.objects.create(
            # category=a['category'],
            name_uz=a['name_uz'],
            name_ru=a['name_ru'],
            name_en=a['name_en'],
            img=a['img'],
            desc_uz=a['desc_uz'],
            desc_ru=a['desc_ru'],
            desc_en=a['desc_en'],
            price=a['price'],
            unit=a['unit'],
            status=a['status'],
        )
        product.save()
        return redirect('/products_list')
    return render(request, 'products/products_add.html')


def products_edit(request, id):
    products = Products.objects.get(id=id)
    product = Products.objects.all()
    if request.method == 'POST':
        a = request.POST
        product.name_uz = a['name_uz']
        # product.name_ru = a['name_ru']
        # product.name_en = a['name_en']
        # product.img = a['img']
        # product.desc_uz = a['desc_uz']
        # product.desc_ru = a['desc_ru']
        # product.desc_en = a['desc_en']
        # product.price = a['price']
        # product.unit = a['unit']
        # product.status = a['status']
        product.save()
        return redirect('/products_list')
    return render(request, "products/products_list.html", {'products': products, 'product': product})


def products_delete(request, id):
    products = Products.objects.get(id=id)
    products.delete()
    return redirect('/products_list')
