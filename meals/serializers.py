from rest_framework import serializers
from .models import Meal, MealIngredient
from inventory.serializers import ItemSerializer

class MealIngredientSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=MealIngredient.objects.none(),  # prevent global queries
        source='item',
        write_only=True
    )

    class Meta:
        model = MealIngredient
        fields = ['id', 'item', 'item_id', 'quantity_needed', 'unit']


class MealSerializer(serializers.ModelSerializer):
    ingredients = MealIngredientSerializer(source='mealingredient_set', many=True, read_only=True)
    is_favorite = serializers.BooleanField(default=False)  

    class Meta:
        model = Meal
        fields = ['id', 'name', 'ingredients', 'created_by', 'is_favorite']
        read_only_fields = ['created_by']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
