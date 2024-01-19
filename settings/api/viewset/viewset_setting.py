from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from settings.api.serializers import SettingsThemeSerializer
from settings.models import Settings


class SettingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SettingsThemeSerializer
    http_method_names = ["get", "post"]

    def get_queryset(self):
        # Filter the queryset to include only settings
        # related to the authenticated user
        return Settings.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Check if settings exist for the user
        existing_settings = Settings.objects.filter(user=self.request.user).first()

        if existing_settings:
            # If settings exist, update them with the new data
            serializer.update(
                existing_settings, validated_data=serializer.validated_data
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # If settings don't exist, create new settings
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
