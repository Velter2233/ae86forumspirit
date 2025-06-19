from django import forms
from spirit.user.auth.forms import RegistrationForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox  # или V2Invisible, если надо
from django.conf import settings


class CustomRegistrationForm(RegistrationForm):
    recaptcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox,
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
        label='Подтвердите, что вы не робот'
    )