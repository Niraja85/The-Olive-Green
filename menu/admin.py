from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Menu, MenuItem

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

@admin.register(MenuItem)
class MenuItemAdmin(SummernoteModelAdmin):
    """Lists field to display menu items"""
    list_display = ('title', 'category', 'price')
    summernote_fields = ('description',)

