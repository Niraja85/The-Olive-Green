from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Table(models.Model):
    """Model to create tables"""
    number = models.PositiveBigIntegerField(unique=True)
    capacity = models.PositiveBigIntegerField()

    def __str__(self):
        return f"Table {self.number} (Seats {self.capacity})"


class Booking(models.Model):
    """Model to create a booking"""
    TIME_CHOICES = (
        (1, "12:00 pm - 1:00 pm"),
        (2, "1:00 pm - 2:45 pm"),
        (3, "3:00 pm - 4:00 pm"),
        (4, "7:00 pm -8:45 pm"),
        (5, "9:00 pm - 10:45 pm")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE,
                              related_name="booking")
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_CHOICES)
    number_of_guests = models.PositiveIntegerField(default=2)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Unique together will ensure to avoid double bookings.
        Order by date and then time"""
        unique_together = ("table", "date", "time")
        ordering = ("date", "time")

        def __str__(self):
            return f"{self.name} | {self.date} {self.time} |Table {self.table.number}"

