# Generated by Django 4.2.4 on 2023-09-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0004_remove_workspace_thumbnail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcomment',
            name='author',
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
    ]
