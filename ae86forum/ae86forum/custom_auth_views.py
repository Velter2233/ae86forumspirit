from django.shortcuts import render, redirect
from django.contrib.auth import login
from ae86forum.forms import CustomRegisterForm  # создадим на следующем шаге

def custom_register(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("spirit:index")
    else:
        form = CustomRegisterForm()
    return render(request, "custom_register.html", {"form": form})
