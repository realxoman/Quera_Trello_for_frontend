from rest_framework import serializers

from workspace.models import TaskLog


class TaskLogSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages[
                    "required"
                ] = f"فیلد \
                `{field.label}` الزامی است."

    class Meta:
        model = TaskLog
        fields = ["id", "task", "old_priority", "new_priority"]
