from rest_framework import serializers
from .models import Meal, MealIngredient
from inventory.models import Item

class MealIngredientSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)

    class Meta:
        model = MealIngredient
        fields = ['id', 'item', 'item_name', 'quantity_needed', 'unit']


class MealSerializer(serializers.ModelSerializer):
    ingredients = MealIngredientSerializer(source='mealingredient_set', many=True, read_only=True)

    class Meta:
        model = Meal
        fields = ['id', 'name', 'ingredients', 'created_by', 'is_favorite']
        read_only_fields = ['created_by']
