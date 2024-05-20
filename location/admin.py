from django.contrib import admin
from .models import Address, City, Country, Location
from import_export.admin import ImportExportModelAdmin


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ('name', 'create_date')
    list_display_links = ('name', 'create_date')
    search_fields = ('name',)
    ordering = ('-create_date',)


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ('name', "create_date")
    list_display_links = ('name', 'create_date')
    search_fields = ('name',)
    ordering = ('-create_date',)


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'create_date')
    list_display_links = ('name', 'create_date')
    search_fields = ('name',)
    ordering = ('-create_date',)


@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin):
    list_display = ('name', 'phone_number', 'address', 'city', 'country', 'create_date')
    list_display_links = ('name', 'phone_number', 'address', 'city', 'country', 'create_date')
    search_fields = ('name', 'address', 'city', 'country')
    ordering = ('-create_date',)



