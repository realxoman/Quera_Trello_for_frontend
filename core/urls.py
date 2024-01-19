from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("account.api_urls"), name="account_api"),
    path("", include("settings.api_urls"), name="settings_api"),
    path("", include("workspace.api_urls"), name="workspace_api"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api-auth/", include("rest_framework.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
