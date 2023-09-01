from rest_framework import serializers

from workspace.models import TaskAssignee


class TaskAssigneeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskAssignee
        fields = ['id', 'user']

    def create(self, validated_data):
        task_id = self.context['task_id']
        return TaskAssignee.objects.create(
            task_id=task_id, **validated_data)
