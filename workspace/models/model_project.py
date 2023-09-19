from django.db import models
from utils.models import DateBasic
from django.utils.translation import gettext_lazy as _

from .model_workspace import Workspace


class Project(DateBasic):

    workspace = models.ForeignKey(
        Workspace, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(_('نام'), max_length=255)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _("Projects")

    def __str__(self):
        return str(self.name)
