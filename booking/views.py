from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import date
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import BookingForm
from .models import Booking


# User views
class BookingCreateView(CreateView, LoginRequiredMixin):
    """ View to render Crete bookings and
    to allow user to create a booking"""
    model = Booking
    form_class = BookingForm
    template_name = "booking/booking.html"
    success_url = reverse_lazy("manage_booking")
    login_url = "account_login"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.table = form.cleaned_data("table_obj")

        # Clear any existing messages before adding new one"
        storage = messages.get_messages(self.request)
        existing = [msg.message for msg in storage]

        if "Booking created successfully." not in existing:
            messages.success(self.request, "Booking created successfully")
            return super().form_valid(form)


class BookingListView(ListView, LoginRequiredMixin):
    """View to render manage bookings"""
    model = Booking
    template_name = "booking/manage_booking.html"
    context_object_name = "booking"

    def get_queryset(self):
        return Booking.objects.filter(
            user = self.request.user,
            date__gte = date.today()).order_by("date", "time")


# Admin views
class AdminBookingListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    """A view to manage admin booking"""
    model =  Booking
    template_name = "booking/admin_booking.html"
    context_object_name = "booking"

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        queryset = Booking.objects.filter(
            date__gte=date.today()).order_by("date", "time")

        search_query = self.request.GET.get("q")
        date_filter = self.request.GET.get("date")

        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query)
                                       | Q(email__icontains=search_query))

        if date_filter:
            queryset = queryset.filter(date=date_filter)

            return queryset















