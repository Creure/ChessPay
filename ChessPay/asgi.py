import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import MultiplayerOnline.routing  # Importa las rutas de tus aplicaciones

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChessPay.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Ruta HTTP normal para el manejo de peticiones HTTP
    "websocket": AuthMiddlewareStack(
        URLRouter(
            MultiplayerOnline.routing.websocket_urlpatterns  # Rutas para los websockets de tu aplicación
        )
    ),
})
