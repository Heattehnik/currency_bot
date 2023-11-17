from django.db import models

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True, verbose_name="ID Телеграм")
    username = models.CharField(max_length=25, verbose_name="Имя Телеграм")
    first_name = models.CharField(max_length=25, verbose_name="Имя")
    last_name = models.CharField(max_length=25, verbose_name="Фамилия")
    is_subscribed = models.BooleanField(default=False, verbose_name="Подписан на рассылку")
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name="Когда зарегестрирован")

    def __str__(self):
        return f"{self.username} - {self.user_id}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["-registered_at"]
