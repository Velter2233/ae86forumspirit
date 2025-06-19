from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomRegistrationForm

def custom_register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('spirit:index')  # или куда ты хочешь
    else:
        form = CustomRegistrationForm()
    return render(request, 'spirit/user/auth/_register.html', {'form': form})
