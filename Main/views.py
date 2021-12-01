from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.files.storage import FileSystemStorage


# Create your views here.


def service(request):
    serv = Extra.objects.all()
    return render(request, 'service/service.html', {'serv': serv})


def service_edit(request, id):
    ex = Extra.objects.get(id=id)
    ext = Extra.objects.all()
    if request.method == 'POST':
        a = request.POST
        ext.name = a["name"]
        ext.quantity = a["quantity"]
        ext.save()
        return redirect('/service')
    return render(request, 'service/service_edit.html', {'ex': ex, 'extra': ext})


def service_add(request):
    if request.method == "POST":
        a = request.POST
        ser = Extra.objects.create(
            name=a['name'],
            quantity=a['quantity'],
        )
        ser.save()
        return redirect('/service')
    return render(request, 'service/service_add.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def log_in(request):
    # print(request.POST)
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect('/dashboard')
    else:
        return render(request, 'login.html')


def izoh(request):
    return render(request, 'izoh.html')


def category_list(request):
    client = Users.objects.all()
    category = Categories.objects.all()
    return render(request, 'category/category_list.html', {'categories': category, 'client': client})


def category_add(request):
    if request.method == "POST" and request.FILES['img']:
        print(request.FILES)
        upload_photo = request.FILES['img']
        fss = FileSystemStorage()
        file = fss.save(upload_photo.name, upload_photo)
        file_url = fss.url(file)
        a = request.POST
        cat = Categories.objects.create(
            name_uz=a['name_uz'],
            name_ru=a['name_ru'],
            name_en=a['name_en'],
            img=file_url
        )
        cat.save()
        return redirect('/category_list')
    return render(request, 'category/category_add.html', {})


def category_edit(request, id):
    category = Categories.objects.get(id=id)
    categories = Categories.objects.all()
    if request.method == 'POST':
        a = request.POST
        category.name_uz = a["name_uz"]
        category.name_ru = a["name_ru"]
        category.name_en = a["name_en"]
        category.img = a["img"]
        category.save()
        return redirect('/category_list')
    return render(request, "category/category_edit.html", {'category': categories, 'categories': category})


def category_del(request, id):
    category = Categories.objects.get(id=id)
    category.delete()
    return redirect('/category_list')


def users(request):
    bot_user = Users.objects.all()
    return render(request, 'users.html', {'bot_user': bot_user})


def products_list(request):
    products = Products.objects.all()
    return render(request, 'products/products_list.html', {'products': products})


def products_add(request):
    print(request.POST)
    category = Categories.objects.all()
    if request.method == "POST":
        a = request.POST
        product = Products.objects.create(
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
    return render(request, 'products/products_add.html', {'category': category})


def products_edit(request, id):
    category = Categories.objects.all()
    product = Products.objects.get(id=id)
    products = Products.objects.all()
    if request.method == 'POST':
        a = request.POST
        product.name_uz = a['name_uz']
        product.name_ru = a['name_ru']
        product.name_en = a['name_en']
        product.img = a['img']
        product.desc_uz = a['desc_uz']
        product.desc_ru = a['desc_ru']
        product.desc_en = a['desc_en']
        product.price = a['price']
        product.unit = a['unit']
        product.status = a['status']
        product.save()
        return redirect('/products_list')
    return render(request, "products/products_edit.html",
                  {'products': product, 'product': products, 'category': category})


def products_delete(request, id):
    products = Products.objects.get(id=id)
    products.delete()
    return redirect('/products_list')


def orders_list(request):
    return render(request, 'orders/orders_list.html')
