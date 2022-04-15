from django.contrib import admin

from .models import devices


@admin.register(devices)
class DevicesAdmin(admin.ModelAdmin):
    pass
