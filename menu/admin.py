from django.contrib import admin
from .models import Menu

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Class to display menu items on admin page"""
    list_display = (
        'name',
        'created_by',
        'active',
    )
    list_filter = ('name',)
