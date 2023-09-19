from django.db import models
from django.contrib.auth import get_user_model
from utils.models import DateBasic
from django.utils.translation import gettext_lazy as _

from .model_workspace import Workspace


class WorkspaceMember(DateBasic):

    workspace = models.ForeignKey(
        Workspace, on_delete=models.CASCADE, related_name='workspace_members')
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name=_('کاربر'),)
    role = models.CharField(_('نقش‌کاربری'), max_length=350)

    class Meta:
        verbose_name = _('Workspace Member')
        verbose_name_plural = _("Workspace Members")

    def __str__(self):
        return str(self.workspace)
