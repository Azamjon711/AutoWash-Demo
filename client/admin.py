from django.contrib import admin
from .models import Address, Client, Comment
from import_export.admin import ImportExportModelAdmin

@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ('name', 'create_date')
    list_display_links = ('name', 'create_date')
    search_fields = ('name',)
    ordering = ('-create_date',)


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('text_length', 'create_date',)
    list_display_links = ('text_length', 'create_date',)
    search_fields = ('text_length',)
    ordering = ('-create_date', )

    def text_length(self, obj):
        return obj.text[:15]


@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'username', 'profession', )
    list_display_links = ('first_name', 'last_name', 'email', 'username', 'profession', )
    search_fields = ('first_name', 'last_name', 'email', 'username', 'profession', )
    ordering = ('-create_date',)







