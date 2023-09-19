from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class ChangePasswordSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = f'فیلد \
                `{field.label}` الزامی است.'

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("new_password1"):
            raise serializers.ValidationError("passwords doesn't match")
        try:
            validate_password(attrs.get("new_password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(
                {"new_password": list(e.messages)})
        return super().validate(attrs)
