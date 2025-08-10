from django.contrib import admin
from .models import Booking


# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Class to view bookings on Admin panel"""
    list_display = (
        "name",
        "date",
        "time",
        "number_of_guests"
    )
    search_fields = (
        "name",
        "date",
        "phone"
    )
