from django.contrib import admin

from .models import EmailSubscriber


@admin.register(EmailSubscriber)
class AdminEmailSubscriber(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'geo', 'date_subscribe']
    list_display_links = ['name', 'phone', 'email', 'geo', 'date_subscribe']
    list_filter = ['geo']
    search_fields = ['geo', 'date_subscribe']
