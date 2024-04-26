from django.urls import path
from .views import *
urlpatterns = [
    path('online/white', white),
    path('online/black', black),
    path('', home),
   path('create/match', CreateMatch)
]
