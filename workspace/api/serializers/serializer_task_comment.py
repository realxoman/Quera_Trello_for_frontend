from rest_framework import serializers

from workspace.models import TaskComment


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ["id", "author", "attachment", "text"]

    def create(self, validated_data):
        task_id = self.context["task_id"]
        return TaskComment.objects.create(task_id=task_id, **validated_data)
