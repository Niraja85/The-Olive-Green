from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookingCreateView.as_view(), name='booking'),
    path("manage/", views.BookingListView.as_view(), name='manage_booking'),
    path("admin/manage/", views.AdminBookingListView.as_view(),
         name='admin_booking'),
]