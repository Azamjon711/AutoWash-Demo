from django.urls import path
from .views import BlogPageView, BlogDetailPageView

urlpatterns = [
    path("blog/", BlogPageView.as_view(), name="blog"),
    path("blog/detail/<slug:slug>/", BlogDetailPageView.as_view(), name="blog-detail"),

]