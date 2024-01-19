from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {"no_active_account": "نام کاربری یا رمز عبور اشتباه است."}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages[
                    "required"
                ] = f"فیلد \
                `{field.label}` الزامی است."

    def validate(self, attrs):
        validated_data = super().validate(attrs)

        # Check if authentication succeeded
        if not self.user:
            # Authentication failed, raise a custom error message
            raise serializers.ValidationError("نام کاربری یا رمز عبور اشتباه است")

        validated_data["user_id"] = self.user.id
        validated_data["username"] = self.user.username
        validated_data["email"] = self.user.email
        validated_data["first_name"] = self.user.first_name
        validated_data["last_name"] = self.user.last_name
        validated_data["phone_number"] = self.user.phone_number
        try:
            validated_data["thumbnail"] = self.user.thumbnail.url
        except Exception:
            validated_data["thumbnail"] = ""

        return validated_data
