from rest_framework import serializers

from workspace.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = f'فیلد `{field.label}` الزامی است.'


    class Meta:
        model = Project
        fields = ['id', 'name']

    def create(self, validated_data):
        workspace_id = self.context['workspace_id']
        return Project.objects.create(
            workspace_id=workspace_id, **validated_data)
