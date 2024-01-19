from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


MAX_SIZE = "2"


def validate_file_size(value):
    # Maximum file size in bytes (e.g., 10 MB)
    max_size = MAX_SIZE * 1024 * 1024  # 10 MB

    if value.size > max_size:
        raise ValidationError(_(f"حجم فایل نباید از {MAX_SIZE} مگابایت بیشتر باشید"))
