"""
URL configuration for tixhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from tixhub import view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(("base.urls", "base"),"base")),
    path('more/<int:movie_id>', view.more_details, name='more_details'),
    path('ticket_booking/<int:movie_id>', view.ticket_booking, name='ticket_booking'),
    path('booking_success/<int:booking_id>', view.booking_success, name='booking_success'),
    path('get_booked_seats/<int:movie_id>/<int:theatre_id>/<str:date>/<str:time>/', view.get_booked_seats, name='get_booked_seats')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)