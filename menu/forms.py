from django import forms
from .models import Menu, MenuItem


class MenuForm(forms.ModelForm):
    """ Form to create Menu """
    class Meta:
        model = Menu
        fields = ['name', 'active']


class MenuItemForm(forms.ModelForm):
    """
    Form to create menu items with checkboxes
    """
    class Meta:
        model = MenuItem
        fields = ['menu', 'title', 'category', 'description', 'price']
        labels = {
            "title": "Title",
            "category": "Category",
            "description": "Description",
            "price": "Price",
        }
