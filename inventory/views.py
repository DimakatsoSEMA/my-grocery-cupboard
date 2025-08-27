from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django.db.models import F
from collections import defaultdict

class ItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return items added by the logged-in user
        return Item.objects.filter(added_by=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the creator to the logged-in user
        serializer.save(added_by=self.request.user)

class ItemRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensure users can only access their own items
        return Item.objects.filter(added_by=self.request.user)

# Grocery list generation for low-stock items
@api_view(['GET'])
def grocery_list(request):
    low_items = Item.objects.filter(
        added_by=request.user,
        quantity__lte=F('low_stock_threshold')
    )

    grouped = defaultdict(list)
    for item in low_items:
        serializer = ItemSerializer(item)
        grouped[item.location].append(serializer.data)

    # Convert defaultdict to regular dict
    grouped_dict = dict(grouped)
    return Response(grouped_dict)

