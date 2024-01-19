from django.contrib import admin
from workspace.models import TaskComment


@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ("task", "author", "text", "created_at", "updated_at")
    search_fields = ("task", "author", "text")

    fieldsets = (("Main", {"fields": ("task", "author", "text")}),)

    add_fieldsets = (("Main", {"fields": ("task", "author", "text")}),)
