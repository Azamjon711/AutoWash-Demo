from django.shortcuts import render, redirect
from django.views import View
from .models import Client
from django.contrib.auth.mixins import LoginRequiredMixin

class ClientListView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "auth/login.html")
        else:
            search = request.GET.get("search")
            if not search:
                clients = Client.objects.all()
                context = {
                    "clients": clients,
                    "search": search,
                }
                return render(request, "main/service.html", context)
            else:
                clients = Client.objects.filter(first_name__icontains=search)
                if clients:
                    context = {
                        "clients": clients,
                        "search": search,
                    }
                    return render(request, "main/service.html", context)
                else:
                    return render(request, "main/404.html")
