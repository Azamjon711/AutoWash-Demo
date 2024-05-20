from django.contrib import admin
from .models import Staff
from import_export.admin import ImportExportModelAdmin


@admin.register(Staff)
class StaffAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'username', 'position', 'image', 'create_date', )
    list_display_links = ('first_name', 'last_name', 'email', 'username', 'position', 'image', 'create_date', )
    search_fields = ('first_name', 'last_name', 'email', 'username', 'position', )
    ordering = ('-create_date', )



