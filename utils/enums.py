from django.db import models


class PermissionEnum(models.IntegerChoices):
    FULL = 4
    EDITOR = 3
    COMMENTOR = 2
    VIEWER = 1