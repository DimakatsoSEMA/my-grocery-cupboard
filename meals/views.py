from rest_framework import generics, permissions
from .models import Meal
from .serializers import MealSerializer

class MealListCreateView(generics.ListCreateAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Meal.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class MealRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Meal.objects.filter(created_by=self.request.user)
