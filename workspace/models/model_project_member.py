from django.db import models
from django.contrib.auth import get_user_model
from utils.models import DateBasic
from django.utils.translation import gettext_lazy as _

from .model_project import Project


class ProjectMember(DateBasic):

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='project_members')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Project Member')
        verbose_name_plural = _("Project Members")

    def __str__(self):
        return str(self.project)
