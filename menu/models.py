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
    ("salads", "Salads"),
    ("cocktails", "Cocktails"),
    ("wine", "Wine"),
    ("desserts", "Desserts"),
    ("chefs special", "Chef's Special")
)
