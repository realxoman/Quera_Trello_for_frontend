from django.db import models
from django.utils.translation import gettext_lazy as _
from account.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
