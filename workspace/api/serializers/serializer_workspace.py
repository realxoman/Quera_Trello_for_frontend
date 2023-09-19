from rest_framework import serializers

from workspace.models import Workspace


class WorkspaceSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = f'فیلد \
                    `{field.label}` الزامی است.'

    class Meta:
        model = Workspace
        fields = ['id', 'name', 'color']

        def create(self, validated_data):
            print("Validation errors:", self.errors)
