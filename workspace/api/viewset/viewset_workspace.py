from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from workspace.models import Workspace, WorkspaceMember
from workspace.api.serializers import WorkspaceSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Workspaces"])
class WorkspaceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkspaceSerializer
    lookup_field = "id"

    def get_queryset(self):
        """
        Return a QuerySet of Workspaces to which the authenticated user has access.
        """
        user = self.request.user
        # Find workspace IDs to which the user has access
        workspace_ids = WorkspaceMember.objects.filter(user=user).values_list(
            "workspace_id", flat=True
        )

        # Return a filtered QuerySet of workspaces
        return Workspace.objects.filter(id__in=workspace_ids)

    def perform_create(self, serializer):
        user = self.request.user
        workspace = serializer.save(creator=user)
        WorkspaceMember.objects.create(
            workspace=workspace, user=user, is_super_access=True
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "حذف موفقیت آمیز بود"}, status=status.HTTP_200_OK)
