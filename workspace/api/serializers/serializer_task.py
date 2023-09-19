from rest_framework import serializers

from workspace.models import Task


class TaskSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = f'فیلد `{field.label}` الزامی است.'


    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'deadline', 'priority', 'order']

    def create(self, validated_data):
        board_id = self.context['board_id']
        return Task.objects.create(
            board_id=board_id, **validated_data)
