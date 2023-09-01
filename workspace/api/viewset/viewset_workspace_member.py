from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from workspace.models import WorkspaceMember
from workspace.api.serializers import WorkspaceMemberSerializer


class WorkspaceMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkspaceMemberSerializer

    def get_queryset(self):
        return WorkspaceMember.objects.filter(
            workspace_id=self.kwargs['workspace_pk'])

    def get_serializer_context(self):
        return {'workspace_id': self.kwargs['workspace_pk']}
