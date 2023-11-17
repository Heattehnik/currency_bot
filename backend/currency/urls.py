from django.urls import path
from currency.apps import CurrencyConfig
from currency.views import LatestCurrencyView

app_name = CurrencyConfig.name

urlpatterns = [
    path('currency', LatestCurrencyView.as_view(), name='latest_currency'),
    # Другие URL-шаблоны вашего приложения...
]
