from rest_framework import serializers

from workspace.models import ProjectMember


class ProjectMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectMember
        fields = ['id', 'user']

    def create(self, validated_data):
        project_id = self.context['project_id']
        return ProjectMember.objects.create(
            project_id=project_id, **validated_data)
