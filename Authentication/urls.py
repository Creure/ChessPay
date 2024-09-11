from django.urls import path
from .views import *

urlpatterns = [
   path("login/", Authentication.as_view()),
   path("register/", Registration.as_view()),
   path("logout/", logout_view),
   path('a2b52c5559b9cb41f24911a614047b6c3d84cb58fc2c1aa8d1fc67deea578ef9/', disabled)
   
]

