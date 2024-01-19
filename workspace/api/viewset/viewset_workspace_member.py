from rest_framework import viewsets, status
from rest_framework.response import Response

from workspace.api.serializers.serializer_workspace_member import (
    WorkspaceMemberCreateSerializer,
)
from workspace.models import WorkspaceMember
from workspace.api.serializers import WorkspaceMemberSerializer

from drf_spectacular.utils import extend_schema
from utils.enums import PermissionEnum
from account.permissions import ProjectMemberPermission


@extend_schema(tags=["Workspace Members"])
class WorkspaceMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [ProjectMemberPermission]
    required_permission = PermissionEnum.FULL
    serializer_class = WorkspaceMemberSerializer

    def get_queryset(self):
        return WorkspaceMember.objects.filter(workspace_id=self.kwargs["workspace_id"])

    def get_serializer_context(self):
        return {"workspace_id": self.kwargs["workspace_id"]}

    def get_serializer_class(self):
        if self.action == "create":
            return WorkspaceMemberCreateSerializer
        return WorkspaceMemberSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "حذف موفقیت آمیز بود"}, status=status.HTTP_200_OK)
