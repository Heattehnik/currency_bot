from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=35, verbose_name="телефон", **NULLABLE)
    chat_id = models.IntegerField(default=0, verbose_name="id чата")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
