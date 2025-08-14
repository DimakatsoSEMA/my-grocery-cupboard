from django.db import models
from django.contrib.auth.models import User

class Location(models.TextChoices):
    FRIDGE = 'Fridge'
    FREEZER = 'Freezer'
    CUPBOARD = 'Cupboard'

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)  # e.g., grams, ml, pieces
    location = models.CharField(max_length=50, choices=Location.choices)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

