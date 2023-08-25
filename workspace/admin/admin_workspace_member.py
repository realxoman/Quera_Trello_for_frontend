from django.contrib import admin
from workspace.models import WorkspaceMember


@admin.register(WorkspaceMember)
class WorkspaceMemberAdmin(admin.ModelAdmin):
    list_display = ('workspace', 'user', 'role', 'created_at', 'updated_at')
    search_fields = ('workspace', 'user', 'role')

    fieldsets = (
        ('Main',
         {'fields': ('workspace', 'user', 'role')}),
    )

    add_fieldsets = (
        ('Main',
         {'fields': ('workspace', 'user', 'role')}),
    )
