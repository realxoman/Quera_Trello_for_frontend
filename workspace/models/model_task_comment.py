from django.db import models
from utils.models import DateBasic
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .model_task import Task


class TaskComment(DateBasic):

    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='task_comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(_("text"), max_length=500, blank=True)

    class Meta:
        verbose_name = _('Task Comment')
        verbose_name_plural = _("Task Comments")

    def __str__(self):
        return str(self.author)
