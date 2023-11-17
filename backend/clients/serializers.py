from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('user_id', 'username', 'first_name', 'last_name', 'is_subscribed', 'registered_at')
        read_only_fields = ('registered_at',)
