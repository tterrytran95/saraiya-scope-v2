"""
ASGI config for scope project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from saraiyascope.routing import museum_urlpatterns
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scope.settings')

print('asdfa', URLRouter(museum_urlpatterns))

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket' : AuthMiddlewareStack(URLRouter(museum_urlpatterns)),
})