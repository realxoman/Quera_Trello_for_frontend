from django.contrib import admin
from workspace.models import TaskAssignee


@admin.register(TaskAssignee)
class TaskAssigneeAdmin(admin.ModelAdmin):
    list_display = ('Task', 'user', 'created_at', 'updated_at')
    search_fields = ('Task', 'user')

    fieldsets = (
        ('Main',
         {'fields': ('Task', 'user')}),
    )

    add_fieldsets = (
        ('Main',
         {'fields': ('Task', 'user')}),
    )
