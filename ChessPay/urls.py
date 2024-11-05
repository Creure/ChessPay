
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MultiplayerOnline.urls')),
    path('', include('Authentication.urls')),
    path('', include('ChessCoin.urls')),
    path('', include('UserInformationManager.urls')),
     path('', include('PayPal_ChessCoin.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)