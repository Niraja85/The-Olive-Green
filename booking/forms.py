from django import forms
from .models import Booking
from datetime import datetime
from django.core.exceptions import ValidationError


class BookingForm(forms.ModelForm):
    """Form to create and edit a booking"""
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'email', 'date',
                  'time', 'number_of_guests', 'message']
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.Select(choices=Booking.TIME_CHOICES),
            'message': forms.Textarea(
                attrs={'placeholder': 'Leave any message to let us know',
                       'rows': 4}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = datetime.now().date()
        self.fields['date'].widget.attrs['min'] = today.strftime('%Y-%m-%d')

    def clean(self):
        """Get form data and clean, check capacity and
        throw errors when table is not available
        """
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")
        number_of_guests = cleaned_data.get("number_of_guests")

        if not date or not time or not number_of_guests:
            raise ValidationError("Please fill in all the required fields")
        if date and date < datetime.now().date():
            self.add_error("date", "Booking date cannot be in the past")

        return cleaned_data
