# Generated by Django 4.2.4 on 2023-09-26 11:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("workspace", "0009_board_is_archive_task_attachment_task_thumbnail_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="taskassignee",
            old_name="Task",
            new_name="task",
        ),
    ]
