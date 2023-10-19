from django.db import models

class Device(models.Model):
    TYPE_CHOICES = [
        ('router', 'router'),
        ('switch', 'switch'),
        ('nas', 'nas'),
        ('epdu', 'epdu'),
        ('proxmox', 'proxmox'),
        ('wlan', 'wlan'),
        ('network_monitor', 'network_monitor')
    ]

    device_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='router')
    name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    link = models.URLField(blank=True, null=True)

    brand = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)

    ssid = models.CharField(max_length=255, blank=True, null=True, verbose_name="SSID")
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    domain = models.URLField(verbose_name="ePDU Domain", blank=True, null=True)

    def __str__(self):
        return self.name
