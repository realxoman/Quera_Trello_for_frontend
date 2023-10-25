from rest_framework import generics, status
from rest_framework.response import Response
from workspace.api.serializers import (
    SubscriptionSerializer,
    SubscriptionInvitationSerializer,
)
from utils.send_email import Util
import uuid

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Subscription"])
class SubscriptionViewSet(generics.GenericAPIView):
    serializer_class = SubscriptionSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        workspace_invitation = serializer.save()
        url = f"https://domain.com/workspace/invitation/{workspace_invitation.token}"
        email_body = f"""
            سلام، شما برای عضویت در یک پروژه‌ی جدید دعوت شده‌اید.
            از طریق این لینک وارد شوید:

            {url}
        """
        email = serializer.validated_data["email"]
        data = {
            "email_body": email_body,
            "to_email": email,
            "email_subject": "عضویت در پروژه جدید",
        }

        Util.send_email(data)

        return Response({"detail": "ایمیل ارسال شد"}, status=status.HTTP_200_OK)


@extend_schema(tags=["Subscription"])
class SubscriptionInvitationViewSet(generics.GenericAPIView):
    serializer_class = SubscriptionInvitationSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        workspace_invitation = serializer.save()

        return Response({"detail": "دعوت انجام شد."}, status=status.HTTP_200_OK)
