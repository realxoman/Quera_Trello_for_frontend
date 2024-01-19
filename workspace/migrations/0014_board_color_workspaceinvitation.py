# Generated by Django 4.2.4 on 2023-10-25 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("workspace", "0013_alter_projectmember_role_alter_task_attachment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="color",
            field=models.CharField(default="#000", max_length=256, verbose_name="رنگ"),
        ),
        migrations.CreateModel(
            name="WorkspaceInvitation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "token",
                    models.CharField(max_length=1000, verbose_name="Invitation token"),
                ),
                ("expired", models.BooleanField(default=False, verbose_name="Expired")),
                (
                    "workspace",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workspace_invitation",
                        to="workspace.workspace",
                    ),
                ),
            ],
            options={
                "verbose_name": "Workspace invitation",
                "verbose_name_plural": "Workspace invitation",
            },
        ),
    ]
