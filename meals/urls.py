from django.urls import path
from .views import MealListCreateView, MealRetrieveUpdateDeleteView

urlpatterns = [
    path('', MealListCreateView.as_view(), name='meal-list-create'),
    path('<int:pk>/', MealRetrieveUpdateDeleteView.as_view(), name='meal-detail'),
]
