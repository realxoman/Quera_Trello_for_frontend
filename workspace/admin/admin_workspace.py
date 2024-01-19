from django.contrib import admin
from workspace.models import Workspace


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "creator", "created_at", "updated_at")
    search_fields = ("name", "creator")

    fieldsets = (
        ("Main", {"fields": ("name", "creator", "thumbnail", "thumbnail_alt")}),
    )

    add_fieldsets = (
        ("Main", {"fields": ("name", "creator", "thumbnail", "thumbnail_alt")}),
    )
