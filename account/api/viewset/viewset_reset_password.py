from django.urls import reverse
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from account.api.serializers import ResetPasswordSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Account Forget Password"])
class ResetPasswordViewSet(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = RefreshToken.for_user(user).access_token
        url = request.build_absolute_uri(reverse("account_urls:reset-password-confirm"))
        return Response(
            {"success": "ایمیل بازیابی ارسال شد", "url": f"{url}?token={token}"},
            status=status.HTTP_200_OK,
        )
