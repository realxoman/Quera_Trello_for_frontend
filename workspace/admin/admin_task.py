from django.contrib import admin
from workspace.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "board",
        "name",
        "deadline",
        "priority",
        "order",
        "created_at",
        "updated_at",
    )
    search_fields = ("board", "name", "description")

    # deadline is not editable so it can't be added
    fieldsets = (
        ("Main", {"fields": ("board", "name", "description", "priority", "order")}),
    )

    add_fieldsets = (
        ("Main", {"fields": ("board", "name", "description", "priority", "order")}),
    )
