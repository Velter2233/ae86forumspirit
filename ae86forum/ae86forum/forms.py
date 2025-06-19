from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegistrationForm(UserCreationForm):
    consent = forms.BooleanField(
        label="Я даю согласие на обработку персональных данных",
        error_messages={"required": "Необходимо согласие с условиями"}
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
