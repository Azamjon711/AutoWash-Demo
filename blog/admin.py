from django.contrib import admin
from .models import Date, Year, Creator, Comments, BlogPost
from import_export.admin import ImportExportModelAdmin

@admin.register(Date)
class DateAdmin(ImportExportModelAdmin):
    list_display = ('date',)
    list_display_links = ('date',)
    ordering = ('-date',)


@admin.register(Year)
class YearAdmin(ImportExportModelAdmin):
    list_display = ('year',)
    list_display_links = ('year',)
    ordering = ('-year',)


@admin.register(Creator)
class CreatorAdmin(ImportExportModelAdmin):
    list_display = ('name', 'image', 'description_length',)
    list_display_links = ('name', 'image', 'description_length',)
    search_fields = ('name', 'description',)

    def description_length(self, obj):
        return obj.description[:15]

@admin.register(Comments)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('text_length', 'create_date',)
    list_display_links = ('text_length', 'create_date',)
    search_fields = ('text_length', )

    def text_length(self, obj):
        return obj.text[:15]


@admin.register(BlogPost)
class BlogPostAdmin(ImportExportModelAdmin):
    list_display = ('title', 'image', 'date', 'creator', 'slug', 'category', 'text_length', )
    list_display_links = ('title', 'image', 'date', 'creator', 'slug', 'category', 'text_length', )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'creator',)

    def text_length(self, obj):
        return obj.text[:15]



