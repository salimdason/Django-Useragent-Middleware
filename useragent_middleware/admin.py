import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from .models import devices


@admin.register(devices)
class DevicesAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        stat_data = (
            devices.objects.annotate().values('windows', 'mac', 'iphone', 'android', 'other')
        )

        as_json = json.dumps(list(stat_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"stat_data":as_json}

        return super().changelist_view(request, extra_context=extra_context)