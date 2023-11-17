from django.contrib import admin
from currency.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'rate', 'date')

