from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from workspace.models import TaskComment
from workspace.api.serializers import TaskCommentSerializer


class TaskCommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskCommentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return TaskComment.objects.filter(
            task_id=self.kwargs['task_id'])

    def get_serializer_context(self):
        return {'task_id': self.kwargs['task_id']}
