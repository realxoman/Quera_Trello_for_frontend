from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from workspace.models import TaskAssignee
from workspace.api.serializers import TaskAssigneeSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Task Members"])
class TaskAssigneeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskAssigneeSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return TaskAssignee.objects.filter(
            task_id=self.kwargs['task_id'])

    def get_serializer_context(self):
        return {'task_id': self.kwargs['task_id']}
