from utils.models import DateBasic
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .model_workspace import Workspace


class WorkspaceInvitation(DateBasic):
    token = models.CharField(max_length=1000, verbose_name=_("Invitation token"))
    workspace = models.ForeignKey(
        Workspace, on_delete=models.CASCADE, related_name="workspace_invitation"
    )
    expired = models.BooleanField(verbose_name=("Expired"), default=False)

    class Meta:
        verbose_name = _("Workspace invitation")
        verbose_name_plural = _("Workspace invitation")
