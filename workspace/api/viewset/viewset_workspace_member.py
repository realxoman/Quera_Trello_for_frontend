from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from workspace.models import WorkspaceMember
from workspace.api.serializers import WorkspaceMemberSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Workspace Members"])
class WorkspaceMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkspaceMemberSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return WorkspaceMember.objects.filter(
            workspace_id=self.kwargs['workspace_id'])

    def get_serializer_context(self):
        return {'workspace_id': self.kwargs['workspace_id']}
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "حذف موفقیت آمیز بود"}, status=status.HTTP_200_OK)
