from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from workspace.models import TaskLog
from workspace.api.serializers import TaskLogSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Task Logs"])
class TaskLogViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskLogSerializer
    lookup_field = 'id'
    http_method_names = ['get']

    def get_queryset(self):
        return TaskLog.objects.filter(
            task_id=self.kwargs['task_id']).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
