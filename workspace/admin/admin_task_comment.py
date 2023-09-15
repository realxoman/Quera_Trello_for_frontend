from django.contrib import admin
from workspace.models import TaskComment


@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('task',  'text', 'created_at', 'updated_at')
    search_fields = ('task', 'text')

    fieldsets = (
        ('Main',
         {'fields': ('task',  'text')}),
    )

    add_fieldsets = (
        ('Main',
         {'fields': ('task',  'text')}),
    )
