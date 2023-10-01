from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from workspace.models import TaskAssignee
from workspace.api.serializers import TaskAssigneeSerializer
from utils.enums import PermissionEnum
from account.permissions import ProjectMemberPermission

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Task Members"])
class TaskAssigneeViewSet(viewsets.ModelViewSet):
    permission_classes = [ProjectMemberPermission]
    required_permission = PermissionEnum.VIEWER
    serializer_class = TaskAssigneeSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return TaskAssignee.objects.filter(
            task_id=self.kwargs['task_id'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "حذف موفقیت آمیز بود"}, status=status.HTTP_200_OK)

    def get_serializer_context(self):
        return {'task_id': self.kwargs['task_id']}
