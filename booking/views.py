from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Booking
from datetime import date
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q


# User views
class BookingCreateView(CreateView, LoginRequiredMixin):
    """ View to render Crete bookings and
    to allow user to create a booking"""
    model = Booking

