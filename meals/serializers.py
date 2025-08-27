from rest_framework import serializers
from .models import Meal, MealIngredient
from inventory.models import Item

class MealIngredientSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())

    class Meta:
        model = MealIngredient

class MealSerializer(serializers.ModelSerializer):
    ingredients = MealIngredientSerializer(many=True)  

    class Meta:
        model = Meal
        fields = ['id', 'name', 'ingredients', 'created_by', 'is_favorite']
        read_only_fields = ['created_by']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        validated_data['created_by'] = self.context['request'].user
        meal = Meal.objects.create(**validated_data)

        for ingredient_data in ingredients_data:
            MealIngredient.objects.create(meal=meal, **ingredient_data)

        return meal
        fields = ['id', 'item', 'item_name', 'quantity_needed', 'unit']

