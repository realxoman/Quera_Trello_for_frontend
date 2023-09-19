from rest_framework import serializers

from workspace.models import TaskAssignee


class TaskAssigneeSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = f'فیلد \
                `{field.label}` الزامی است.'

    class Meta:
        model = TaskAssignee
        fields = ['id', 'user']

    def create(self, validated_data):
        task_id = self.context['task_id']
        return TaskAssignee.objects.create(
            task_id=task_id, **validated_data)
