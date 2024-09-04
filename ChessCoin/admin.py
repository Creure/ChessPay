from django.contrib import admin
from .models import BankInformation
# Register your models here.

@admin.register(BankInformation)
class BankInformationAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank_name', 'account_number')