from django.urls import path
from .views import *
urlpatterns = [
    path('chess/<str:ID>', chess),
    path('join/<str:id_info>', join),
    path('wallet/', wallet),
    path('profile/', profile),
    path('<int:page>/', lobbies),
   path('create/match/<str:amount>/<str:piece>', CreateMatch)
]
