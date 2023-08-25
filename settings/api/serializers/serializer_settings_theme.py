from rest_framework import serializers

from settings.models import Settings


class SettingsThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Settings
        fields = ['id', 'theme']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
