from django.urls import path
from django.urls import include

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls"))
]
