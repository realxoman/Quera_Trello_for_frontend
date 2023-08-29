from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from workspace.models import Workspace
from workspace.api.serializers import WorkspaceSerializer


class WorkspaceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer