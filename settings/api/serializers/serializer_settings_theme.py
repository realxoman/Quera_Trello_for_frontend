from rest_framework import serializers

from settings.models import Settings


class SettingsThemeSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = f'فیلد \
                `{field.label}` الزامی است.'

    class Meta:
        model = Settings
        fields = ['id', 'theme']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
