from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from workspace.models import Board
from django.db import models
from workspace.api.serializers import BoardSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Boards"])
class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Board.objects.filter(
            project_id=self.kwargs['project_id']).order_by('order')

    def get_serializer_context(self):
        return {'project_id': self.kwargs['project_id']}

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        if 'order' in data:
            new_order = int(data['order'])
            boards = self.get_queryset()
            old_order = instance.order

            if new_order < old_order:
                boards.filter(
                    order__gte=new_order, order__lt=old_order).update(
                    order=models.F('order') + 1)
            elif new_order > old_order:
                boards.filter(
                    order__gt=old_order, order__lte=new_order).update(
                    order=models.F('order') - 1)

            instance.order = new_order
            instance.save()

        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)
