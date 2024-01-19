from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse

from workspace.api.serializers import (
    SubscriptionSerializer,
    SubscriptionInvitationSerializer,
    SubscriptionCopySerializer,
)
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Subscription"])
class SubscriptionViewSet(generics.GenericAPIView):
    serializer_class = SubscriptionSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        workspace_invitation = serializer.save()
        url = self.request.build_absolute_uri(
            reverse(
                "workspace:workspace_router:subscriptions_invitation",
                args=[workspace_invitation.token],
            )
        )
        return Response({"detail": url}, status=status.HTTP_200_OK)


@extend_schema(tags=["Subscription"])
class SubscriptionCopyViewSet(generics.GenericAPIView):
    serializer_class = SubscriptionCopySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        workspace_invitation = serializer.save()
        url = self.request.build_absolute_uri(
            reverse(
                "workspace:workspace_router:subscriptions_invitation",
                args=[workspace_invitation.token],
            )
        )
        return Response(
            {"detail": "لینک دعوت ساخته شده.", "url": url}, status=status.HTTP_200_OK
        )


@extend_schema(tags=["Subscription"])
class SubscriptionInvitationViewSet(generics.GenericAPIView):
    serializer_class = SubscriptionInvitationSerializer

    def get(self, request, token):
        serializer = self.serializer_class(
            data={"token": token}, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "دعوت انجام شد."}, status=status.HTTP_200_OK)
