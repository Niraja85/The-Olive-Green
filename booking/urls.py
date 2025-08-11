from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookingCreateView.as_view(), name='booking'),
    path("manage/", views.BookingListView.as_view(), name='manage_booking'),
    path("edit/<int:pk>/", views.BookingUpdateView.as_view(),
         name='edit_booking'),
    path("delete/<int:pk>/", views.BookingDeleteView.as_view(),
         name='confirm_delete_booking'),
]