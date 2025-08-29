from django.urls import path
from .views import (
    ItemListCreateView, 
    ItemRetrieveUpdateDeleteView,
    grocery_list,
    item_list_view,
    grocery_list_view
)

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDeleteView.as_view(), name='item-detail'),
    path('grocery-list/', grocery_list, name='grocery-list'),
    path('items-ui/', item_list_view, name='item-list'),
    path('grocery-list-ui/', grocery_list_view, name='grocery-list-view'),
]
