from django import forms
from spirit.user.auth.forms import RegistrationForm
from django_recaptcha.fields import ReCaptchaField


class CustomRegistrationForm(RegistrationForm):
    captcha = ReCaptchaField()