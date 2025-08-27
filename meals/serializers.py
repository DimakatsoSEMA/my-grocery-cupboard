from rest_framework import serializers
from .models import Meal, MealIngredient
from inventory.serializers import ItemSerializer

class MealIngredientSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = MealIngredient
        fields = ['item', 'quantity_needed', 'unit']

class MealSerializer(serializers.ModelSerializer):
    ingredients = MealIngredientSerializer(source='mealingredient_set', many=True, read_only=True)

    class Meta:
        model = Meal
        fields = ['id', 'name', 'ingredients', 'created_by']
        read_only_fields = ['created_by']

    def create(self, validated_data):
        user = self.context['request'].user
        meal = Meal.objects.create(created_by=user, **validated_data)
        return meal
