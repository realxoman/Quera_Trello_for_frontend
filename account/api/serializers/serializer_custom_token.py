from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data['user_id'] = self.user.id
        validated_data['username'] = self.user.username
        validated_data['email'] = self.user.email
        validated_data['first_name'] = self.user.first_name
        validated_data['last_name'] = self.user.last_name

        return validated_data
