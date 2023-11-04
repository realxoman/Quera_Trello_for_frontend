from django.contrib import admin
from account.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser',)
    list_filter = ('is_staff', 'is_superuser',)
    search_fields = ('username', 'email')

    fieldsets = (
        ('Personal', {'fields': ('username', 'email', 'password',
         'phone_number', 'first_name', 'last_name', 'thumbnail')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        ('Personal', {'fields': ('username', 'email', 'password',
         'phone_number', 'first_name', 'last_name', 'thumbnail')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
