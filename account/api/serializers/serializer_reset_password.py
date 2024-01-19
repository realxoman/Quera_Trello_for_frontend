from rest_framework import serializers
from account.models import CustomUser
from django.core.exceptions import ValidationError


class ResetPasswordSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages[
                    "required"
                ] = f"فیلد \
                `{field.label}` الزامی است."

    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ["email"]

    def validate(self, attrs):
        try:
            user = CustomUser.objects.get(email=attrs["email"])
        except CustomUser.DoesNotExist:
            raise ValidationError({"detail": "There is no user with provided email"})
        attrs["user"] = user
        return super().validate(attrs)
