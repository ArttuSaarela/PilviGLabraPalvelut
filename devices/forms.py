from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_type', 'name', 'ip_address', 'link', 'brand', 'model', 'ssid', 'username', 'password', 'domain']