from django.contrib import admin
from workspace.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "workspace", "name", "created_at", "updated_at")
    search_fields = ("workspace", "name")

    fieldsets = (("Main", {"fields": ("workspace", "name")}),)

    add_fieldsets = (("Main", {"fields": ("workspace", "name")}),)
