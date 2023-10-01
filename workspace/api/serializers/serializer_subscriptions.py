from rest_framework import serializers
from django.core.exceptions import ValidationError
from account.models import CustomUser
import jwt
from django.conf import settings


class SubscriptionSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = f'فیلد \
                `{field.label}` الزامی است.'

    email = serializers.CharField(max_length=500)
    url = serializers.CharField(max_length=300)

    class Meta:
        model = CustomUser
        fields = ['url', 'email']