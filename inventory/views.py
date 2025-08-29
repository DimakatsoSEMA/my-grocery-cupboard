from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django.db.models import F
from collections import defaultdict
from django.shortcuts import render
from django.contrib.auth import get_user_model

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

#fRONTEND - UI
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class DemoItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = []  # no authentication needed

    def get_queryset(self):
        demo_user = User.objects.get(username="demo")  # always use demo user
        return Item.objects.filter(added_by=demo_user)

    def perform_create(self, serializer):
        demo_user = User.objects.get(username="demo")
        serializer.save(added_by=demo_user)


from django.shortcuts import get_object_or_404, redirect, render
from .models import Item
from django.contrib.auth import get_user_model
from .forms import ItemForm 

User = get_user_model()

def item_list_view(request):
    """
    View for /items-ui/
    Shows all items for the demo user, grouped by location
    """
    demo_user = User.objects.get(username="demo")  # built-in demo user
    items = Item.objects.filter(added_by=demo_user)
    
    # Optional: group by location for better display
    grouped_items = {}
    for item in items:
        grouped_items.setdefault(item.location, []).append(item)
    
    return render(request, "inventory/item_list.html", {"grouped_items": grouped_items})


def grocery_list_view(request):
    """
    View for /grocery-list-ui/
    Shows low-stock items for the demo user, grouped by location
    """
    demo_user = User.objects.get(username="demo")  # built-in demo user
    all_items = Item.objects.filter(added_by=demo_user)
    
    # Filter low-stock items using the model property
    low_stock_items = [item for item in all_items if item.is_low_stock]
    
    # Group by location
    grouped_items = {}
    for item in low_stock_items:
        grouped_items.setdefault(item.location, []).append(item)
    
    return render(request, "inventory/grocery_list.html", {"grouped_items": grouped_items})

def item_update_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item-list')
    else:
        form = ItemForm(instance=item)
    return render(request, "inventory/item_form.html", {"form": form})

def item_delete_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item-list')
    return render(request, "inventory/item_confirm_delete.html", {"item": item})
