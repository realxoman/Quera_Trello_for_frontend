from rest_framework import serializers

from account.api.serializers import UserSerializer
from account.models import CustomUser
from workspace.models import WorkspaceMember


class WorkspaceMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = WorkspaceMember
        fields = ["id", "user", "is_super_access"]


class WorkspaceMemberCreateSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=CustomUser.objects.all(),
        slug_field="username",
    )

    class Meta:
        model = WorkspaceMember
        fields = ["id", "user", "is_super_access"]

    def validate(self, attrs):
        if WorkspaceMember.objects.filter(
            workspace_id=self.context["workspace_id"], user=attrs["user"]
        ).exists():
            raise serializers.ValidationError(
                "این کاربر قبلا به این پروژه اضافه شده است"
            )
        return attrs

    def create(self, validated_data):
        workspace_id = self.context["workspace_id"]
        return WorkspaceMember.objects.create(
            workspace_id=workspace_id, **validated_data
        )
