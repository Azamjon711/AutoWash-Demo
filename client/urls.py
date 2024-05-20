from django.urls import path
from .views import ClientListView

urlpatterns = [
    path("service/", ClientListView.as_view(), name="service"),

]
