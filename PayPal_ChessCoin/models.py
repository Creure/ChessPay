from django.db import models
from django.utils import timezone
from Authentication.models import User
from django.utils.translation import gettext_lazy as _

import hashlib

class ImmutableFieldsModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk:
            original = self.__class__.objects.get(pk=self.pk)
            for field in self._meta.fields:
                field_name = field.name
                if getattr(original, field_name) != getattr(self, field_name):
                    raise ValueError(f"El campo '{field_name}' no puede ser modificado después de la creación")
        super().save(*args, **kwargs)

class PayPalTransaction(models.Model):
    payment_id = models.CharField(max_length=255, primary_key=True)
    payer_id = models.CharField(max_length=255)
    state = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    merchant_id = models.CharField(max_length=255, blank=True, null=True)
    hash = models.CharField(max_length=64)
    ChessCoin_SKU = models.CharField(max_length=255, default='N/A')
    Nush_ChessCoin = models.BinaryField(null=True)  
    create_time = models.DateTimeField(default=timezone.now)  
    update_time = models.DateTimeField(default=timezone.now)  
    identification_number = models.CharField(max_length=20, verbose_name=_("Identification Number"), default='N/A')

    class Meta:
        verbose_name = 'PayPal Transaction'
        verbose_name_plural = 'PayPal Transactions'

    

  

    def __str__(self):
        return f"Transaction {self.payment_id} - {self.amount} {self.currency}"
