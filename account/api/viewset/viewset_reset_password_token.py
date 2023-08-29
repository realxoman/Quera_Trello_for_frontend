from rest_framework import generics, status
from rest_framework.response import Response
from account.api.serializers import ResetPasswordTokenSerializer


class ResetPasswordTokenViewSet(generics.GenericAPIView):
    serializer_class = ResetPasswordTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {"detail": "Token is valid"}, status=status.HTTP_200_OK)
