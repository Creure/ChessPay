from django.urls import path
from .views import *

urlpatterns = [
   path("profile/update/GUI/", gui_update)

]

