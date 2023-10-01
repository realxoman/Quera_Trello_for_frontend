from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "حذف موفقیت آمیز بود"}, status=status.HTTP_200_OK)
