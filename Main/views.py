from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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
        return redirect('/index')
    else:
        return render(request, 'login.html')

def general(request):
    return render(request, 'general.html')

def advanced(request):
    return render(request, 'advanced.html')

def table(request):
    return render(request, 'data.html')