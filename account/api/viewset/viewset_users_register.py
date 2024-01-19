from rest_framework import viewsets, status
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from account.api.serializers import UserRegisterSerializer, UserSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Account Details"])
class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer
    http_method_names = ["get", "post", "delete", "patch"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserRegisterSerializer
        return UserSerializer

    @extend_schema(tags=["Account Register"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=["Account Update"])
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_email = request.data.get("email")
        if (
            new_email
            and get_user_model()
            .objects.filter(email=new_email)
            .exclude(pk=instance.pk)
            .exists()
        ):
            return Response(
                {"email": ["این ایمیل توسط کاربر دیگری در حال استفاده است."]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(tags=["Account Delete"])
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "حذف موفقیت آمیز بود"}, status=status.HTTP_200_OK)
