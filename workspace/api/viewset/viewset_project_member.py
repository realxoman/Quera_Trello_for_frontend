from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from workspace.models import ProjectMember
from workspace.api.serializers import ProjectMemberSerializer


class ProjectMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectMemberSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return ProjectMember.objects.filter(
            project_id=self.kwargs['project_pk'])

    def get_serializer_context(self):
        return {'project_id': self.kwargs['project_pk']}
