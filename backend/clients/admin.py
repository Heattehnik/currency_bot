from django.contrib import admin
from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'registered_at', 'is_subscribed')

