from spirit.user.auth.forms import RegistrationForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.conf import settings


class CustomRegistrationForm(RegistrationForm):
    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)