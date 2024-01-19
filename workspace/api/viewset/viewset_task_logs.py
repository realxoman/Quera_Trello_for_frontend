from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from workspace.models import TaskLog
from workspace.api.serializers import TaskLogSerializer

from drf_spectacular.utils import extend_schema
from utils.enums import PermissionEnum
from account.permissions import ProjectMemberPermission


@extend_schema(tags=["Task Logs"])
class TaskLogViewSet(viewsets.ModelViewSet):
    permission_classes = [ProjectMemberPermission]
    required_permission = PermissionEnum.VIEWER
    serializer_class = TaskLogSerializer
    lookup_field = "id"
    http_method_names = ["get"]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "حذف موفقیت آمیز بود"}, status=status.HTTP_200_OK)

    def get_queryset(self):
        return TaskLog.objects.filter(task_id=self.kwargs["task_id"]).order_by(
            "-created_at"
        )

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
