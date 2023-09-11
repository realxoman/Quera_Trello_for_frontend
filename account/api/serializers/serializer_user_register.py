from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password']

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
        return user
