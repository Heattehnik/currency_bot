from django.db import models

from clients.models import Client
from currency.models import Currency


class Request(models.Model):
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="request", verbose_name="Запрос")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="request", verbose_name="Валюта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return f"{self.created_at} - {self.user_id}"

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"
        ordering = ["-created_at"]
