from django.urls import path
from .views import TeamPageView

urlpatterns = [
    path("team/", TeamPageView.as_view(), name="team"),

]
