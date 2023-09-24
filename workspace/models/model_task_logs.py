from django.db import models
from utils.models import DateBasic
from django.utils.translation import gettext_lazy as _

from .model_task import Task


class TaskLog(DateBasic):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, verbose_name=_('Task'))
    old_priority = models.IntegerField(
        default=0, verbose_name=_('Old Priority'))
    new_priority = models.IntegerField(
        default=0, verbose_name=_('New Priority'))

    class Meta:
        verbose_name = _('Task Log')
        verbose_name_plural = _("Task Logs")

    def __str__(self):
        return self.name
