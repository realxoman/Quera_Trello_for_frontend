from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from workspace.models import TaskAssignee
from workspace.api.serializers import TaskAssigneeSerializer


class TaskAssigneeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskAssigneeSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return TaskAssignee.objects.filter(
            task_id=self.kwargs['task_pk'])

    def get_serializer_context(self):
        return {'task_id': self.kwargs['task_pk']}
