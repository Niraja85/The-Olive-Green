from django.db import models
from django.contrib.auth.models import User



class Menu (models.Model):
    """ Model to create menu """
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        """ Order by name """
        ordering = ['name']

    def __str__(self):
        return self.name

MENU_CATEGORIES = (
    ("starter", "Starter"),
    ("main", "Main"),
    ("cocktails", "Cocktails"),
    ("wine", "Wine"),
    ("desserts", "Desserts"),
    ("chefs special", "Chef's Special")
)

class MenuItem (models.Model):
    """ Models to create menu items """
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50,choices=MENU_CATEGORIES, default='starter')
    description = models.TextField(default="")
    price = models.FloatField(default=0.00)

class Meta:
    """ Ordering by category and title """
    ordering = ['category', 'title']

def __str__(self):
    return self.title

