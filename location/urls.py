from django.urls import path
from .views import WashingPointsPageView

urlpatterns = [
    path("location/", WashingPointsPageView.as_view(), name="location"),

]
