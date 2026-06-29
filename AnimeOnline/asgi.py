"""
ASGI config for AnimeOnline project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os
import django

# from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AnimeOnline.settings')
# django.setup()

# from main import routing
application = get_asgi_application()

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     # "websocket": 
# })