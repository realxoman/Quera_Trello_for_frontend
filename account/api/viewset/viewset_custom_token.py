from rest_framework_simplejwt.views import TokenObtainPairView

from account.api.serializers import CustomTokenObtainPairSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Authentication"])
class CustomTokenObtainPairViewSet(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
