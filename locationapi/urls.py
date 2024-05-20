from django.urls import path, include
from .views import AddressAPIViewSet, CityAPIViewSet, CountryAPIViewSet, LocationAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register("address", viewset=AddressAPIViewSet)
router.register("city", viewset=CityAPIViewSet)
router.register("country", viewset=CountryAPIViewSet)
router.register("location", viewset=LocationAPIViewSet)


urlpatterns = [
    path("", include(router.urls)),

]
