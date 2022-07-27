from django.urls import path
from .consumers import MuseumConsumer
museum_urlpatterns = [
    path('route/MUSEUM/', MuseumConsumer.as_asgi())
]

