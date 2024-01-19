from rest_framework import serializers

from account.models import CustomUser
from workspace.models import ProjectMember
from account.api.serializers import UserSerializer


class ProjectMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ProjectMember
        fields = ["id", "user"]


class ProjectMemberCreateSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField("username", queryset=CustomUser.objects.all())

    class Meta:
        model = ProjectMember
        fields = ["id", "user"]

    def validate(self, attrs):
        if ProjectMember.objects.filter(
            project_id=self.context["project_id"], user=attrs["user"]
        ).exists():
            raise serializers.ValidationError(
                "این کاربر قبلا به این پروژه اضافه شده است"
            )
        return attrs

    def create(self, validated_data):
        project_id = self.context["project_id"]
        return ProjectMember.objects.create(project_id=project_id, **validated_data)
