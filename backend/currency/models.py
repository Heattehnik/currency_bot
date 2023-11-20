from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=10, verbose_name='Код валюты')
    name = models.CharField(max_length=50, verbose_name='Наименование валюты')
    rate = models.DecimalField(max_digits=10, decimal_places=4, verbose_name='Стоимость')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return f"Курс доллара на {self.date} - {self.rate} руб."

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = "Курсы валют"
        ordering = ["-date"]
