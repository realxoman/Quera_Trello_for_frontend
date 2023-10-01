from rest_framework import serializers

from account.permissions import ProjectMemberPermission
from utils.enums import PermissionEnum

from workspace.models import WorkspaceMember


class WorkspaceMemberSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the error message for required fields
        for field_name, field in self.fields.items():
            if field.required:
                field.error_messages['required'] = f'فیلد \
                    `{field.label}` الزامی است.'

    class Meta:
        model = WorkspaceMember
        fields = ['id', 'user', 'role']

    def create(self, validated_data):
        workspace_id = self.context['workspace_id']
        return WorkspaceMember.objects.create(
            workspace_id=workspace_id, **validated_data)
