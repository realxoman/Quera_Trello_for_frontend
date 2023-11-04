from rest_framework import serializers

from workspace.models import ProjectMember
from account.api.serializers import UserSerializer


class ProjectMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = f'فیلد \
                `{field.label}` الزامی است.'

    class Meta:
        model = ProjectMember
        fields = ['id', 'user']

    def create(self, validated_data):
        project_id = self.context['project_id']
        return ProjectMember.objects.create(
            project_id=project_id, **validated_data)
