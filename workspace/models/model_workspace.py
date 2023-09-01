from django.db import models
from django.contrib.auth import get_user_model
from utils.models import DateBasic
from django.utils.translation import gettext_lazy as _


class Workspace(DateBasic):

    name = models.CharField(_('name'), max_length=255)
    creator = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='workspaces')
    thumbnail = models.ImageField(_('thumbnail'), blank=True, null=True)
    thumbnail_alt = models.CharField(
        _('thumbnail alt'), max_length=350, blank=True
        )

    class Meta:
        verbose_name = _('Workspace')
        verbose_name_plural = _("Workspaces")

    def __str__(self):
        return self.name
