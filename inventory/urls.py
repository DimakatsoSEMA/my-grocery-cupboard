from django.urls import path
from .views import (
    ItemListCreateView, 
    ItemRetrieveUpdateDeleteView,
    grocery_list
)

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDeleteView.as_view(), name='item-detail'),
    path('grocery-list/', grocery_list, name='grocery-list'),  
]
