from django import forms
from .models import Menu, MenuItem

class MenuForm(forms.ModelForm):
    """ Form to create Menu """
    class Meta:
        model = Menu
        fields = [
            'name',
            'active',
        ]