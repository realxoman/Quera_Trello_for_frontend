from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.models import DateBasic
from .model_project import Project


class Board(DateBasic):

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='boards')
    name = models.CharField(_('نام'), max_length=200)
    order = models.BigIntegerField(_("ترتیب"), default=0)

    class Meta:
        verbose_name = _('Board')
        verbose_name_plural = _("Boards")

    def __str__(self):
        return self.name
