# Generated by Django 4.2.4 on 2023-10-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0005_alter_customuser_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to="profile_pics",
                verbose_name="تصویر پروفایل",
            ),
        ),
    ]