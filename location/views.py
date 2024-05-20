from django.shortcuts import render
from django.views import View
from .models import Location
from django.contrib.auth.mixins import LoginRequiredMixin


class WashingPointsPageView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "auth/login.html")
        else:
            search = request.GET.get("search")
            if not search:
                locations = Location.objects.all()
                context = {
                    "locations": locations,
                    "search": search,
                }
                return render(request, "main/location.html", context)
            else:
                locations = Location.objects.filter(address__name__icontains=search)
                if locations:
                    context = {
                        "locations": locations,
                        "search": search,
                    }
                    return render(request, "main/location.html", context)
                else:
                    return render(request, "main/404.html")

