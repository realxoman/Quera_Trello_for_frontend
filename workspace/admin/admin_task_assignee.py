from django.contrib import admin
from workspace.models import TaskAssignee


@admin.register(TaskAssignee)
class TaskAssigneeAdmin(admin.ModelAdmin):
    list_display = ("task", "user", "created_at", "updated_at")
    search_fields = ("task", "user")

    fieldsets = (("Main", {"fields": ("task", "user")}),)

    add_fieldsets = (("Main", {"fields": ("task", "user")}),)
