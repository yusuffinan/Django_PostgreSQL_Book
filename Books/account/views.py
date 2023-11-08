from django.shortcuts import redirect, render
from  .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect("category_list")
        else:
            return render(request, "account/login.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})


def user_register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_")
        else:
            return render(request, "account/register.html", {"form": form})
    else:
        form = RegisterForm()
        return render(request, "account/register.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login_")