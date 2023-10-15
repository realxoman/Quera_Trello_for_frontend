from rest_framework.response import Response
from rest_framework import generics, status
# from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from utils.send_email import (
    Util
)
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
        # relativeLink = reverse('account_urls:reset-password-confirm')
        current_site = 'localhost:3000/'
        absurl = 'http://'+current_site+'Reset-password/'+"?token="+str(token)
        email_body = 'سلام '+user.email + \
            '\nاز لینک زیر برای تغییر رمز عبور خود استفاده کنید. \n' + absurl
        data = {
            'email_body': email_body,
            'to_email': user.email,
            'email_subject': 'تایید تغییر رمز عبور'
        }

        Util.send_email(data)
        return Response({'success':
                        "ایمیل بازیابی ارسال شد"},
                        status=status.HTTP_200_OK)
