from django.urls import path
from django.urls import include
from .views import authView
from .views import home

urlpatterns = [
    path("", home, name = "home"),
    path("signup/", authView, name = "authView"),
    path("accounts/", include("django.contrib.auth.urls")),
]
