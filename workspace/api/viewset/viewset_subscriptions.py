from rest_framework import generics, status
from rest_framework.response import Response
from workspace.api.serializers import SubscriptionSerializer

from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Subscription"])
class SubscriptionViewSet(generics.GenericAPIView):
    serializer_class = SubscriptionSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {"detail": "ایمیل ارسال شد"}, status=status.HTTP_200_OK)
