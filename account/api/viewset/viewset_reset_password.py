from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from utils.send_email import (
    Util
)
from account.api.serializers import ResetPasswordSerializer


class ResetPasswordViewSet(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = RefreshToken.for_user(user).access_token
        relativeLink = reverse('account_urls:reset-password-confirm')
        current_site = get_current_site(
            request=request).domain
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.email + \
            '\nUse the link below to reset your password \n' + absurl
        data = {
            'email_body': email_body,
            'to_email': user.email,
            'email_subject': 'Verify your email'
        }

        Util.send_email(data)
        return Response({'success':
                        'We have sent you a link to reset your password'},
                        status=status.HTTP_200_OK)
