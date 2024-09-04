from django.db import models
from Authentication.models import User  # Importa el User desde Authentication.models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Masculino'), ('female', 'Femenino'), ('other', 'Otro')], blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    id_card_number = models.CharField(max_length=50, blank=True, null=True)
    gui = models.BooleanField(default=False) #False =android True=desktop
    verified = models.BooleanField(default=False)  # Campo para verificar el perfil

    def __str__(self):
        return self.full_name or self.user.username
