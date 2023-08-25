from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.api_urls'), name='account_api'),
    path('', include('settings.api_urls'), name='settings_api'),
    path('', include('workspace.api_urls'), name='workspace_api'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc/', SpectacularRedocView.as_view(
        url_name='schema'), name='redoc'),
    path('', SpectacularSwaggerView.as_view(
        url_name='schema'), name='swagger-ui'),
]
