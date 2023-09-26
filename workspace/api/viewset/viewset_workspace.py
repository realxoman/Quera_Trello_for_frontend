from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from workspace.models import Workspace
from workspace.api.serializers import WorkspaceSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Workspaces"])
class WorkspaceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
