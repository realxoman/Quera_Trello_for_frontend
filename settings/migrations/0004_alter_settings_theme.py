# Generated by Django 4.2.4 on 2023-09-19 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_settings_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='theme',
            field=models.CharField(default=0, max_length=10, verbose_name='رنگ تم'),
        ),
    ]
