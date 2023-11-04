from rest_framework import serializers

from workspace.models import Board, Task
from workspace.api.serializers.serializer_task import TaskSerializer


class BoardSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    tasks_count = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = f'فیلد \
                `{field.label}` الزامی است.'

    class Meta:
        model = Board
        fields = ['id', 'name', 'order', 'tasks', 'tasks_count', 'is_archive', 'color']

    def get_tasks(self, obj):
        tasks = Task.objects.filter(board_id=obj.id)
        return TaskSerializer(tasks, many=True).data

    def get_tasks_count(self, obj):
        task_count = Task.objects.filter(board_id=obj.id).count()
        return task_count

    def create(self, validated_data):
        project_id = self.context['project_id']
        return Board.objects.create(
            project_id=project_id, **validated_data)
