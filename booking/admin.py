from django.contrib import admin
from .models import Table, Booking


# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """Class to view tables in Admin panel"""
    list_display = (
        "number",
        "capacity"
    )
    list_filter = (
        "number",
        "capacity"
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Class to view bookings on Admin panel"""
    list_display = (
        "name",
        "date",
        "time",
        "table",
        "number_of_guests"
    )
    list_filter = (
        "date",
        "table"
    )
    search_fields = (
        "name",
        "date",
        "phone"
    )
