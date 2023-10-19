from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Olettaen, että sinulla on näkymä nimeltä 'login'
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, 'home.html')