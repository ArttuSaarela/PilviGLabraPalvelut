from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('add', views.add_device, name='add_device'),
    path('add_device/', views.add_device, name='add_device'),
    path('', views.list_devices.as_view(), name='list_devices'),
    path('detail/<int:device_id>/', views.device_detail, name='device_detail'),
    path('edit/<int:device_id>/', views.edit_device, name='edit_device'),
    path('remove/<int:pk>/', staff_member_required(views.LaiteDeleteView.as_view()), name='device_remove'),
]
