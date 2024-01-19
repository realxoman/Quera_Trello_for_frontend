from rest_framework import serializers

from workspace.models import Task, TaskAssignee
from workspace.api.serializers.serializer_task_assignee import TaskAssigneeSerializer


class TaskSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "description",
            "deadline",
            "priority",
            "attachment",
            "thumbnail",
            "order",
            "members",
            "created_at",
        ]

    def create(self, validated_data):
        board_id = self.context["board_id"]
        return Task.objects.create(board_id=board_id, **validated_data)

    def get_members(self, obj):
        members = TaskAssignee.objects.filter(task=obj)
        return TaskAssigneeSerializer(members, many=True).data
