from django.contrib import admin
from workspace.models import ProjectMember


@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'role', 'created_at', 'updated_at')
    search_fields = ('project', 'user')

    fieldsets = (
        ('Main',
         {'fields': ('project', 'user', 'role')}),
    )

    add_fieldsets = (
        ('Main',
         {'fields': ('project', 'user', 'role')}),
    )
