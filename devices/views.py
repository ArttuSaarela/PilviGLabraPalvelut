from django.shortcuts import render, redirect, get_object_or_404
from .models import Device
from .forms import DeviceForm
from django.views.generic import ListView, edit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def list_routers(request):
    routers = Device.objects.filter(device_type='router')
    return render(request, 'devices/router_list.html', {'routers': routers})

@staff_member_required
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_devices')  # assuming 'list_devices' is the name of a view you want to redirect to after adding a device
    else:
        form = DeviceForm()

    context = {
        'form': form,
    }
    
    return render(request, 'devices/add_device.html', context)

def device_detail(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    return render(request, 'devices/device_detail.html', {'device': device})

@staff_member_required
def edit_device(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    if request.method == "POST":
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('device_detail', device_id=device.id)
    else:
        form = DeviceForm(instance=device)
    return render(request, 'devices/edit_device.html', {'form': form})

class list_devices(LoginRequiredMixin, ListView):
    template_name = "devices/device_list.html"
    context_object_name = "device_types"

    def get_queryset(self):
        device_dict = {}
        for device in Device.objects.all():
            current_type = device.device_type.lower()
            # if current type is not in dict yet
            if current_type not in device_dict:
                device_dict[current_type] = []
            device_dict[current_type].append(device)
        return device_dict


class LaiteDeleteView(edit.DeleteView):
    model = Device
    success_url = reverse_lazy('list_devices')