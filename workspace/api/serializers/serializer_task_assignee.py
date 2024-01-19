from rest_framework import serializers

from account.models import CustomUser
from workspace.models import TaskAssignee
from account.api.serializers import UserSerializer


class TaskAssigneeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TaskAssignee
        fields = ["id", "user"]


class TaskAssigneeCreateSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username", queryset=CustomUser.objects.all()
    )

    class Meta:
        model = TaskAssignee
        fields = ["user"]

    def validate(self, attrs):
        if TaskAssignee.objects.filter(
            task_id=self.context["task_id"], user=attrs["user"]
        ).exists():
            raise serializers.ValidationError(
                "این کاربر قبلا به این تسک اختصاص داده شده است"
            )
        return attrs

    def create(self, validated_data):
        task_id = self.context["task_id"]
        return TaskAssignee.objects.create(task_id=task_id, **validated_data)
