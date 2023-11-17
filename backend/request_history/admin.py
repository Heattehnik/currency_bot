from django.contrib import admin
from request_history.models import Request


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'currency', 'created_at')
