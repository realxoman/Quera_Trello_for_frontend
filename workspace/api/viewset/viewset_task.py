from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from workspace.models import Task
from django.db import models
from workspace.api.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(
            board_id=self.kwargs['board_pk']).order_by('order')

    def get_serializer_context(self):
        return {'board_id': self.kwargs['board_pk']}

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        if 'order' in data:
            new_order = int(data['order'])
            tasks = self.get_queryset()
            old_order = instance.order

            if new_order < old_order:
                tasks.filter(order__gte=new_order, order__lt=old_order).update(
                    order=models.F('order') + 1)
            elif new_order > old_order:
                tasks.filter(
                    order__gt=old_order, order__lte=new_order).update(
                    order=models.F('order') - 1)

            instance.order = new_order
            instance.save()

        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)
