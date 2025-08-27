from django.db import models
from django.conf import settings

class Location(models.TextChoices):
    FRIDGE = 'Fridge'
    FREEZER = 'Freezer'
    CUPBOARD = 'Cupboard'

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=50)  # e.g., grams, ml, pieces
    location = models.CharField(max_length=50, choices=Location.choices)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    expiry_date = models.DateField(null=True, blank=True)
    low_stock_threshold = models.FloatField(default=5)

    def __str__(self):
        return self.name

    @property
    def is_low_stock(self):
        return self.quantity < self.low_stock_threshold



