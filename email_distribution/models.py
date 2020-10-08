from django.db import models


class EmailSubscriber(models.Model):
    name = models.CharField(max_length=63, verbose_name="Имя")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")
    geo = models.CharField(max_length=15, verbose_name="Гео подписчика")
    date_subscribe = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    def __str__(self):
        return f'{self.id} - {self.email} - {self.geo}'

    class Meta:
        verbose_name = "Подписчик по почте"
        verbose_name_plural = "Подписчики по почте"


class PageThankYou(models.Model):
    slug = models.SlugField(max_length=7, unique=True, db_index=True, verbose_name="Гео")
    html_page = models.FileField(upload_to="uploads/templates/%Y/%m/%d/")

    def __str__(self):
        return f'{self.slug}'

    class Meta:
        verbose_name = "Страница спасибо"
        verbose_name_plural = "Страницы спасибо"
