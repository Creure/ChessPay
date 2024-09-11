from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class AuthenticationTokenTime(models.Model):
    token_auth = models.CharField(max_length=512, primary_key=True)
    username = models.CharField(max_length=150)
    last_login = models.DateTimeField(default=timezone.now)
    session_time = models.DateTimeField(default=timezone.now)  # Default to current time
    valid_session = models.BooleanField(default=True)
    ip_address = models.CharField(max_length=45)

   

    def __str__(self):
        return self.username


class UserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        
        if username is None:
            username = email
        
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractUser):
    identification_number = models.CharField(max_length=20, unique=True, primary_key=True, verbose_name=_("Identification Number"))
    id_image = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("ID Image"))
    wallet = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name=_("Wallet"))    
    email = models.EmailField(max_length=254, unique=True, verbose_name=_("Email"))
    first_name = models.CharField(max_length=30, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=30, verbose_name=_("Last Name"))
    additional_emails = models.TextField(blank=True, null=True, verbose_name=_("Additional Emails"))
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name=_("Phone Number"))
    id_history = models.JSONField(blank=True, null=True, verbose_name=_("ID History"))
    
    objects = UserManager()

    def __str__(self):
        return self.username




