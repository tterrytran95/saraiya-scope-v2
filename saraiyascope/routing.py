from django.urls import path
from .views import MuseumConsumer

museum_urlpatterns = [
    path('MUSEUM/', MuseumConsumer.as_asgi())
]