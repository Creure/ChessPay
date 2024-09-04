from django.db import models
from django.utils.translation import gettext_lazy as _
from Authentication.models import User

class BankInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bank_info')
    bank_name = models.CharField(max_length=100, verbose_name=_("Bank Name"))
    bank_type = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Bank Type"))
    swift_code = models.CharField(max_length=11, blank=True, null=True, verbose_name=_("SWIFT Code"))
    account_number = models.CharField(max_length=34, blank=True, null=True, verbose_name=_("Account Number"))
    bank_address = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Bank Address"))
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("Phone Number"))
    additional_info = models.TextField(blank=True, null=True, verbose_name=_("Additional Information"))

    def __str__(self):
        return self.bank_name
