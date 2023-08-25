from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from settings.api.serializers import SettingsThemeSerializer
from settings.models import Settings

class SettingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Settings.objects.all()
    serializer_class = SettingsThemeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
