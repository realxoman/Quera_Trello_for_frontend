from rest_framework import viewsets
from django.contrib.auth import get_user_model
from account.api.serializers import UserRegisterSerializer, UserSerializer

from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Account Details"])
class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer
    http_method_names = ['get', 'post', 'delete', 'patch']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserRegisterSerializer
        return UserSerializer

    @extend_schema(tags=["Account Register"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=["Account Update"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(tags=["Account Delete"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
