from django.db import models
from django.utils import timezone

class AuthenticationTokenTime(models.Model):
    token_auth = models.CharField(max_length=255, primary_key=True)
    username = models.CharField(max_length=150)
    last_login = models.DateTimeField(default=timezone.now)
    session_time = models.DateTimeField(default=timezone.now)  # Default to current time
    valid_session = models.BooleanField(default=True)
    ip_address = models.CharField(max_length=45)

   

    def __str__(self):
        return self.username
