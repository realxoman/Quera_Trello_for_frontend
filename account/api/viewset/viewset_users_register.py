from rest_framework import viewsets
from django.contrib.auth import get_user_model
from account.api.serializers import UserRegisterSerializer


class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer
