from django.contrib import admin
from workspace.models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'name', 'created_at', 'updated_at')
    search_fields = ('project', 'name')

    fieldsets = (
        ('Main',
         {'fields': ('project', 'name', 'order')}),
    )

    add_fieldsets = (
        ('Main',
         {'fields': ('project', 'name', 'order')}),
    )
