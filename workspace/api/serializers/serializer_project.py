from rest_framework import serializers

from workspace.models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name']

    def create(self, validated_data):
        workspace_id = self.context['workspace_id']
        return Project.objects.create(
            workspace_id=workspace_id, **validated_data)
