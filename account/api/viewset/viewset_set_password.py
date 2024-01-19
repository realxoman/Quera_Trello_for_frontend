from rest_framework.response import Response
from rest_framework import generics, status

from account.api.serializers import SetPasswordSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Account Forget Password"])
class SetPasswordViewSet(generics.GenericAPIView):
    serializer_class = SetPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"detail": "Password reset successfully"}, status=status.HTTP_200_OK
        )
