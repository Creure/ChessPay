import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import MultiplayerOnline.routing  
import django
django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChessPay.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  
    "websocket": AuthMiddlewareStack(
        URLRouter(
            MultiplayerOnline.routing.websocket_urlpatterns  
        )
    ),
})
