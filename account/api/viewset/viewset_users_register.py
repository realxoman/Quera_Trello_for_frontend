from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from account.api.serializers import UserRegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = get_user_model()
    permission_classes = [IsAuthenticated]
    serializer_class = UserRegisterSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset
