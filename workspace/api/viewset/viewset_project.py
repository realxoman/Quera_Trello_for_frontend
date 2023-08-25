from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from workspace.models import Project
from workspace.api.serializers import ProjectSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Project.objects.filter(workspace_id=self.kwargs['workspace_pk'])

    def get_serializer_context(self):
        return {'workspace_id': self.kwargs['workspace_pk']}
