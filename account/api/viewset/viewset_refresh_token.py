from rest_framework_simplejwt.views import TokenRefreshView

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Authentication"])
class CustomTokenRefreshView(TokenRefreshView):
    pass