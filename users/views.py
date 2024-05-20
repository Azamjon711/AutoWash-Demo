from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from client.views import ClientListView
from client.models import Client
from staff.models import Staff
from location.models import Location
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import BlogPost


class LandingPageView(View):
    def get(self, request):
        clients = Client.objects.all()
        staffs = Staff.objects.all()
        locations = Location.objects.all()
        posts = BlogPost.objects.all()

        context = {
            "clients": clients,
            "staffs": staffs,
            "locations": locations,
            "posts": posts,
        }
        return render(request, "main/index.html", context)


class UserRegisterView(View):
    def get(self, request):
        return render(request, "auth/register.html")

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password_1"]
        confirm_password = request.POST["password_2"]

        if password == confirm_password:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            checkUser = User.objects.filter(username=username, password=password)
            if checkUser:
                return render(request, "auth/register.html")
            else:
                user = User(first_name=first_name, last_name=last_name, email=email, username=username)
                user.set_password(password)
                user.save()
                return redirect('login')
        else:
            return render(request, "auth/register.html")


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {
            "form": form
        }
        return render(request, "auth/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        data = {
            "username": username,
            "password": password
        }

        loginForm = AuthenticationForm(data=data)

        if loginForm.is_valid():
            user = loginForm.get_user()
            login(request, user)
            return redirect("home")
        else:
            form = UserLoginForm()
            context = {
                "form": form
            }
            return render(request, "auth/login.html")


class AboutPageView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "auth/login.html")
        else:
            search = request.GET.get("search")
            if not search:
                staffs = Staff.objects.all()
                context = {
                    "staffs": staffs,
                    "search": search,
                }
                return render(request, "main/about.html", context)
            else:
                staffs = Staff.objects.filter(position__icontains=search)
                if staffs:
                    context = {
                        "staffs": staffs,
                        "search": search,
                    }
                    return render(request, "main/about.html", context)
                else:
                    return render(request, "main/404.html")


class PricePageView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "auth/login.html")
        else:
            return render(request, "main/price.html")


class ContactPageView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "auth/login.html")
        else:
            return render(request, "main/contact.html")


class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")














