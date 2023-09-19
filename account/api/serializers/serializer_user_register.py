from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from settings.models import Settings


class UserRegisterSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = f'فیلد \
                `{field.label}` الزامی است.'

    password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password',
                  'first_name', 'last_name', 'phone_number']

    def validate(self, value):
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError(
                _("The user exists with this username."))
        elif get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError(
                _("The email already register."))
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        settings = Settings.objects.create(user=user, theme=0)
        settings.save()
        return user
