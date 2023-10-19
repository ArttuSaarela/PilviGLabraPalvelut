from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['device_type', 'name', 'ip_address', 'link', 'brand', 'model']
    list_filter = ['device_type', 'brand']
    search_fields = ['name', 'ip_address', 'brand', 'model']