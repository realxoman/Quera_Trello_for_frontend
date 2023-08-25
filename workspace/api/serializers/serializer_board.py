from rest_framework import serializers

from workspace.models import Board


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ['id', 'name', 'order']

    def create(self, validated_data):
        project_id = self.context['project_id']
        return Board.objects.create(
            project_id=project_id, **validated_data)
