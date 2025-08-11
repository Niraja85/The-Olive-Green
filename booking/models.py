from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    """Model to create a booking"""
    TIME_CHOICES = (
        ('12:00', "12:00 pm - 1:00 pm"),
        ('1:00', "1:00 pm - 2:45 pm"),
        ('3:00', "3:00 pm - 4:00 pm"),
        ('7:00', "7:00 pm -8:45 pm"),
        ('9:00', "9:00 pm - 10:45 pm")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.IntegerField(choices=TIME_CHOICES, default=1)
    number_of_guests = models.IntegerField()
    message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Unique together will ensure to avoid double bookings.
        Order by date and then time"""
        unique_together = ("date", "time")
        ordering = ("date", "time")

        def __str__(self):
            return f"{self.name} | {self.date} {self.time}"
