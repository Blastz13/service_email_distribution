from django.db import models


class EmailSubscriber(models.Model):
    name = models.CharField(max_length=63, verbose_name="Имя")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")
    geo = models.CharField(max_length=15, verbose_name="Гео подписчика")
    date_subscribe = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")
