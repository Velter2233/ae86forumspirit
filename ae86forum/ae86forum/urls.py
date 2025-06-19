from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from .views import custom_register

from spirit.user.auth.views import register
from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from ae86forum.categoryviews import home_with_category
from ae86forum.views import custom_register
from ae86forum.forms import CustomRegistrationForm

import spirit.urls

admin.site.login = login_required(admin.site.login)

urlpatterns = [
    path('register/', custom_register, name='custom_register'),
    path('register/', custom_register, name='custom_register'),
    path("", include(spirit.urls)),
    path('custom-home/', home_with_category, name='custom_home'),
    re_path(r"^admin/", admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
