from django.urls import path, include
from .views import AddressAPIViewSet, CommentAPIViewSet, ClientAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register("address", viewset=AddressAPIViewSet)
router.register("comment", viewset=CommentAPIViewSet)
router.register("client", viewset=ClientAPIViewSet)

urlpatterns = [
    path("", include(router.urls)),

]

