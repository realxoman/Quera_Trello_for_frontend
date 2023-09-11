from rest_framework_simplejwt.views import TokenObtainPairView

from account.api.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairViewSet(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
