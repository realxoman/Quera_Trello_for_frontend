# Generated by Django 4.2.4 on 2023-08-15 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("settings", "0002_settings_created_at_settings_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="settings",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="settings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
