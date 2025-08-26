from rest_framework import generics, permissions
from .models import Item
from .serializers import ItemSerializer

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


