from django.contrib import admin
from workspace.models import ProjectMember


@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'created_at', 'updated_at')
    search_fields = ('project', 'user')

    fieldsets = (
        ('Main',
         {'fields': ('project', 'user')}),
    )

    add_fieldsets = (
        ('Main',
         {'fields': ('project', 'user')}),
    )
