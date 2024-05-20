from django.urls import path
from .views import LandingPageView, UserRegisterView, UserLoginView, UserLogOutView, AboutPageView, PricePageView
from .views import ContactPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('price/', PricePageView.as_view(), name="price"),
    path('contact/', ContactPageView.as_view(), name="contact"),
    path('auth/register', UserRegisterView.as_view(), name="register"),
    path('auth/login', UserLoginView.as_view(), name="login"),
    path('auth/logout', UserLogOutView.as_view(), name="logout"),

]
