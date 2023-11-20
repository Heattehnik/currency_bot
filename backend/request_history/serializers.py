from rest_framework import serializers

from currency.models import Currency
from .models import Request


# class CurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Currency
#         fields = ('code', 'name', 'rate', 'date')


class RequestSerializer(serializers.ModelSerializer):
    rate = serializers.ReadOnlyField(source='currency.rate')

    class Meta:
        model = Request
        fields = ["user_id", "rate", "created_at"]
