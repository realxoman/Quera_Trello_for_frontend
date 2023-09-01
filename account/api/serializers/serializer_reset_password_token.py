from rest_framework import serializers
from django.core.exceptions import ValidationError
from account.models import CustomUser
import jwt
from django.conf import settings


class ResetPasswordTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=600)

    class Meta:
        model = CustomUser
        fields = ['token']

    def validate(self, attrs):
        token = attrs['token']
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
            user = CustomUser.objects.get(id=payload['user_id'])
        except jwt.ExpiredSignatureError:
            return ValidationError({'detail': 'Token expired'})

        attrs["user"] = user
        return super().validate(attrs)
