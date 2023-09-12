from rest_framework import serializers

from workspace.models import Workspace


class WorkspaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workspace
        fields = ['id', 'name', 'color']

        def create(self, validated_data):
            print("Validation errors:", self.errors)
