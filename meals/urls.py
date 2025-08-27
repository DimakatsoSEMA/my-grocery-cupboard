from django.urls import path
from .views import MealListCreateView, MealRetrieveUpdateDeleteView

urlpatterns = [
    path('meals/', MealListCreateView.as_view(), name='meal-list-create'),
    path('meals/<int:pk>/', MealRetrieveUpdateDeleteView.as_view(), name='meal-detail'),
]
