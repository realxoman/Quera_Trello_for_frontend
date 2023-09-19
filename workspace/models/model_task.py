from django.db import models
from utils.models import DateBasic
from django.utils.translation import gettext_lazy as _

from .model_board import Board


class Task(DateBasic):

    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(_('نام'), max_length=255)
    description = models.TextField(
        _("توضیحات"), max_length=500, blank=True)
    deadline = models.DateField(_("ددلاین"), auto_now_add=True)
    priority = models.BigIntegerField(_("اولویت"), default=0)
    order = models.BigIntegerField(_("ترتیب"), default=0)

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.name
