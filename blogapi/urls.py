from django.urls import path, include
from .views import DateAPIViewSet, YearAPIViewSet, CreatorAPIViewSet, CommentsAPIViewSet, BlogPostAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register("date", viewset=DateAPIViewSet)
router.register("year", viewset=YearAPIViewSet)
router.register("creator", viewset=CreatorAPIViewSet)
router.register("comments", viewset=CommentsAPIViewSet)
router.register("blogpost", viewset=BlogPostAPIViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", views.obtain_auth_token),

]

