from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from workspace.models import Project
from workspace.api.serializers import ProjectSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Projects"])
class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Project.objects.filter(workspace_id=self.kwargs['workspace_id'])

    def get_serializer_context(self):
        return {'workspace_id': self.kwargs['workspace_id']}
