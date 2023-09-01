from rest_framework import serializers

from workspace.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'deadline', 'priority', 'order']

    def create(self, validated_data):
        board_id = self.context['board_id']
        return Task.objects.create(
            board_id=board_id, **validated_data)
