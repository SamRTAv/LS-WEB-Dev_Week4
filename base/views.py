from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def loginPage(request):
    page = "login"
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are successfully logged in")
                return render(request, "base/home.html")
            else:
                messages.error(request,"Password is wrong")
        except:
            messages.error(request, "Username does not exist")

        

    context = {"page": page}
    return render(request, "base/login.html", context)


def logoutPage(request):
    logout(request)
    messages.success(request, "You are successfully logged out")
    context = {'logoutredirect' : "Y"}
    return render(request, "base/login.html",context)


def RegisterPage(request):
    page = "register"
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if User.objects.filter(username=username):
            # messages.clear()
            messages.warning(request, "Username already exists! PLease try other")

        elif pass1 != pass2:
            # messages.clear()
            messages.error(request, "Both the passwords are not matching")

        else:
            myUser = User.objects.create_user(username, email, pass1)
            myUser.save()
            # messages.clear()
            messages.success(request,"Your account has been successfully created.",)
            return render(request, "base/login.html")

    context = {"page": page}

    return render(request, "base/login.html", context)


def home(request):
    return render(request, "base/home.html")
