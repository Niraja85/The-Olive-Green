from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import date, timedelta
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import BookingForm
from .models import Booking


# User views
class BookingCreateView(LoginRequiredMixin, CreateView):
    """ View to render create bookings and
    to allow user to create a booking"""
    model = Booking
    form_class = BookingForm
    template_name = "booking/booking.html"
    success_url = reverse_lazy("manage_booking")
    login_url = "account_login"

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Clear any existing messages before adding new one"
        storage = messages.get_messages(self.request)
        existing = [msg.message for msg in storage]

        if "Booking created successfully." not in existing:
            messages.success(self.request, "Booking created successfully")
        return super().form_valid(form)


class BookingListView(LoginRequiredMixin, ListView):
    """View to render manage bookings"""
    model = Booking
    template_name = "booking/manage_booking.html"
    context_object_name = "booking"

    def get_queryset(self):
        if self.request.user.is_staff:
            # returns all bookings with date greater than yesterday
            return Booking.objects.filter(
                date__gt=(date.today()-timedelta(days=1))
                )
        else:
            # returns all bookings with logged in customer
            # with date greater than yesterday.
            return Booking.objects.filter(
                user=self.request.user,
                date__gte=(date.today()-timedelta(days=1))
                )


class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View to edit/update bookings by the user via a form"""
    model = Booking
    form_class = BookingForm
    template_name = 'booking/edit_booking.html'
    success_url = reverse_lazy("manage_booking")

    def form_valid(self, form):
        form.instance.user = self.get_object().user
        messages.success(self.request, "Booking updated successfully")
        return super().form_valid(form)

    def test_func(self):
        """ Test user is staff or allow only owner of the booking"""
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().user


class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View to delete the booking"""
    model = Booking
    template_name = 'booking/confirm_delete_booking.html'
    success_url = reverse_lazy("manage_booking")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Booking cancelled successfully.")
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        """Test user is staff or allow only the owner of the booking"""
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().user
