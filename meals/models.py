from django.db import models
from django.conf import settings  
from inventory.models import Item

class Meal(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Item, through='MealIngredient')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class MealIngredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_needed = models.FloatField()
    unit = models.CharField(max_length=50)
