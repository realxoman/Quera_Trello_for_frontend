from rest_framework import serializers

from workspace.models import Workspace


class WorkspaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workspace
        fields = ['id', 'name', 'creator', 'thumbnail', 'thumbnail_alt']

        def create(self, validated_data):
            print("Validation errors:", self.errors)
