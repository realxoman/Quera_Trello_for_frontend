from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from workspace.models import TaskComment
from workspace.api.serializers import TaskCommentSerializer

from drf_spectacular.utils import extend_schema
from utils.enums import PermissionEnum
from account.permissions import ProjectMemberPermission

@extend_schema(tags=["Task Comment"])
class TaskCommentViewSet(viewsets.ModelViewSet):
    permission_classes = [ProjectMemberPermission]
    required_permission = PermissionEnum.COMMENTOR
    serializer_class = TaskCommentSerializer
    lookup_field = 'id'
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        return TaskComment.objects.filter(
            task_id=self.kwargs['task_id'])

    def get_serializer_context(self):
        return {'task_id': self.kwargs['task_id']}

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "حذف موفقیت آمیز بود"}, status=status.HTTP_200_OK)
