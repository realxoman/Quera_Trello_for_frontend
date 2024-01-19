from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from workspace.api.serializers.serializer_project_member import (
    ProjectMemberCreateSerializer,
)
from workspace.models import ProjectMember
from workspace.api.serializers import ProjectMemberSerializer
from drf_spectacular.utils import extend_schema
from utils.enums import PermissionEnum
from account.permissions import ProjectMemberPermission


@extend_schema(tags=["Project Members"])
class ProjectMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [ProjectMemberPermission]
    required_permission = PermissionEnum.FULL
    serializer_class = ProjectMemberSerializer
    lookup_field = "id"

    def get_queryset(self):
        return ProjectMember.objects.filter(project_id=self.kwargs["project_id"])

    def get_serializer_class(self):
        if self.action == "create":
            return ProjectMemberCreateSerializer
        return ProjectMemberSerializer

    def get_serializer_context(self):
        return {"project_id": self.kwargs["project_id"]}

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "حذف موفقیت آمیز بود"}, status=status.HTTP_200_OK)
