from rest_framework import serializers
from account.models import CustomUser
from django.core.exceptions import ValidationError


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        try:
            user = CustomUser.objects.get(email=attrs["email"])
        except CustomUser.DoesNotExist:
            raise ValidationError(
                {"detail": "There is no user with provided email"})
        attrs["user"] = user
        return super().validate(attrs)
