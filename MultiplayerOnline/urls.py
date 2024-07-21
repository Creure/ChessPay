from django.urls import path
from .views import *
urlpatterns = [
    path('chess/<str:ID>', chess),
    
    path('', home),
   path('create/match', CreateMatch)
]
