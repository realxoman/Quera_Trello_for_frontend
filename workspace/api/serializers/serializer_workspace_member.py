from rest_framework import serializers

from workspace.models import WorkspaceMember


class WorkspaceMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkspaceMember
        fields = ['id', 'user', 'role']

    def create(self, validated_data):
        workspace_id = self.context['workspace_id']
        return WorkspaceMember.objects.create(
            workspace_id=workspace_id, **validated_data)
