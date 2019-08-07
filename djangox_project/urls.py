from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from users.views import MySignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/signup/custom/', MySignupView.as_view(), name="account_signup_custom"),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
