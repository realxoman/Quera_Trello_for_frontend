from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings
from account.models import CustomUser


class SetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=600)
    password = serializers.CharField(
        min_length=8, max_length=32, write_only=True)
    password1 = serializers.CharField(
        min_length=8, max_length=32, write_only=True)

    class Meta:
        fields = ['password', 'password1', 'token']

    def validate(self, attrs):

        if attrs["password"] != attrs["password1"]:
            raise serializers.ValidationError(
                {"details": "Passwords does not match"}
            )

        try:
            password = attrs.get('password')
            token = attrs.get('token')
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
            user = CustomUser.objects.get(id=payload['user_id'])
            user.set_password(password)
            user.save()

            return super().validate(attrs)
        except Exception:
            raise AuthenticationFailed('The reset link is invalid', 401)
