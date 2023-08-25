from django.db import models
from django.contrib.auth import get_user_model
from utils.models import DateBasic
from django.utils.translation import gettext_lazy as _


class Settings(DateBasic):

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='settings')
    theme = models.BigIntegerField(_("theme"), default=0)

    class Meta:
        verbose_name = _('Setting')
        verbose_name_plural = _("Settings")

    def __str__(self):
        return str(self.theme)
