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
        widgets = {
            "price": forms.NumberInput(attrs={"min": "0", "step": "0.01"}),
        }

    """
    Prevent negative prices
    """
    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
