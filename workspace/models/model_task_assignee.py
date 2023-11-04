from django.db import models
from django.contrib.auth import get_user_model
from utils.models import DateBasic
from django.utils.translation import gettext_lazy as _

from .model_task import Task


class TaskAssignee(DateBasic):

    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='tasks_assignee')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Task Assignee')
        verbose_name_plural = _("Tasks Assignee")

    def __str__(self):
        return str(self.Task)
