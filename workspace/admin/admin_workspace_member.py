from django.contrib import admin
from workspace.models import WorkspaceMember


@admin.register(WorkspaceMember)
class WorkspaceMemberAdmin(admin.ModelAdmin):
    list_display = ("workspace", "user", "is_super_access", "created_at", "updated_at")
    search_fields = ("workspace", "user", "is_super_access")

    fieldsets = (("Main", {"fields": ("workspace", "user", "is_super_access")}),)

    add_fieldsets = (("Main", {"fields": ("workspace", "user", "is_super_access")}),)
