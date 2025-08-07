from django import forms
from .models import Booking, Table
from datetime import datetime
from django.core.exceptions import ValidationError


class BookingForm(forms.ModelForm):
    """Form to create and edit a booking"""
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'email', 'date',
                  'time', 'number_of_guests', 'message']
        widget = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.Select(choices=Booking.TIME_CHOICES),
            'message': forms.Textarea(
                attrs={'placeholder': 'Leave any message to let us know',
                       'rows': 4}
            ),
        }

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop("user", None)
            super().__init__(*args, **kwargs)
            today = datetime.now().date()
            self.fields['date'].widget.attrs['min'] = today.strftime("%m%d%Y")

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

            # Find tables that are large enough
            customer_tables = Table.objects.filter(
                capacity__gte=number_of_guests)

            # Exclude already booked tables
            customer_tables = customer_tables.exclude(
                booking__date=date,
                booking__time=time,
            )

            if not customer_tables.exists():
                raise ValidationError(
                    "No available tables for this time slot."
                    "Please call us to enquire."
                )

            # attach the first available table so the view can save it
            cleaned_data["table_obj"] = customer_tables.first()
            return cleaned_data
