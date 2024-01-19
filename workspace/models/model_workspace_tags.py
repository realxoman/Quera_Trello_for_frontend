from django.db import models
from django.contrib.auth import get_user_model
from utils.models import DateBasic
from django.utils.translation import gettext_lazy as _

from .model_workspace import Workspace


class WorkspaceTag(DateBasic):
    workspace = models.ForeignKey(
        Workspace, on_delete=models.CASCADE, related_name="workspace_tags"
    )
    name = models.CharField(_("نام"), max_length=255)
    color = models.CharField(_("رنگ"), max_length=256, default="#000")

    class Meta:
        verbose_name = _("Workspace Tag")
        verbose_name_plural = _("Workspace Tags")

    def __str__(self):
        return str(self.workspace)
