from django.db import models
from utils.models import DateBasic
from django.utils.translation import gettext_lazy as _

from .model_workspace import Workspace
from workspace.models.model_project_member import ProjectMember
from utils.enums import PermissionEnum


class Project(DateBasic):
    workspace = models.ForeignKey(
        Workspace, on_delete=models.CASCADE, related_name="projects"
    )
    name = models.CharField(_("نام"), max_length=255)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)

        # Create a ProjectMember with role=PermissionEnum.FULL when a Project is created
        project_member = ProjectMember.objects.create(
            project=self, user=self.workspace.creator, role=PermissionEnum.FULL
        )
        project_member.save()
