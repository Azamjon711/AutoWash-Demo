from django.shortcuts import render
from django.views import View
from .models import Staff
from django.contrib.auth.mixins import LoginRequiredMixin

class TeamPageView(LoginRequiredMixin, View):
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
                return render(request, "main/team.html", context)
            else:
                staffs = Staff.objects.filter(position__icontains=search)
                if staffs:
                    context = {
                        "staffs": staffs,
                        "search": search,
                    }
                    return render(request, "main/team.html", context)
                else:
                    return render(request, "main/404.html")
