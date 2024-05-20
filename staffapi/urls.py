from django.urls import path, include
from .views import StaffAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register("staff", viewset=StaffAPIViewSet)


urlpatterns = [
    path("", include(router.urls)),

]
