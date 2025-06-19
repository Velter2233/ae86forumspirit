from spirit.user.auth.views import register
from .forms import CustomRegistrationForm

def custom_register(request, *args, **kwargs):
    return register(request, form_class=CustomRegistrationForm)