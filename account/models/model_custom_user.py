from django.db import models
from django.utils.translation import gettext_lazy as _
from account.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='profile_pics')
    phone_number_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="The phone number is invalid.")
    phone_number = models.CharField(validators=[phone_number_validator], max_length=11, blank=True, null=True, unique=True)
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
