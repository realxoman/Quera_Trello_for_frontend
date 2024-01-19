from django.db import models
from django.contrib.auth import get_user_model
from utils.models import DateBasic
from django.utils.translation import gettext_lazy as _


class Workspace(DateBasic):
    name = models.CharField(_("نام"), max_length=255)
    creator = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="workspaces"
    )
    color = models.CharField(_("رنگ"), max_length=256, default="#000")

    class Meta:
        verbose_name = _("Workspace")
        verbose_name_plural = _("Workspaces")

    def __str__(self):
        return self.name
