from rest_framework import serializers
from .models import Meal, MealIngredient
from inventory.models import Item

class MealIngredientSerializer(serializers.ModelSerializer):
    # Display item name in response, allow PK in requests
    item_name = serializers.CharField(source='item.name', read_only=True)
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())

    class Meta:
        model = MealIngredient
        fields = ['id', 'item', 'item_name', 'quantity_needed', 'unit']


class MealSerializer(serializers.ModelSerializer):
    # Nested ingredient serializer
    ingredients = MealIngredientSerializer(many=True)

    class Meta:
        model = Meal
        fields = ['id', 'name', 'ingredients', 'created_by', 'is_favorite']
        read_only_fields = ['created_by']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        # created_by will come from context (current user)
        user = self.context['request'].user
        meal = Meal.objects.create(created_by=user, **validated_data)

        for ingredient_data in ingredients_data:
            MealIngredient.objects.create(meal=meal, **ingredient_data)

        return meal

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])

        # Update meal fields
        instance.name = validated_data.get('name', instance.name)
        instance.is_favorite = validated_data.get('is_favorite', instance.is_favorite)
        instance.save()

        # Replace ingredients
        instance.mealingredient_set.all().delete()
        for ingredient_data in ingredients_data:
            MealIngredient.objects.create(meal=instance, **ingredient_data)

        return instance
