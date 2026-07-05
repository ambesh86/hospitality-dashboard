from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

from .models import (
    Transaction,
    Venue,
    TransactionItem,
    Item
)

from .serializers import (
    TransactionSerializer,
    VenueSerializer,
    TransactionItemSerializer,
    ItemSerializer
)


# -----------------------------
# Item API
# -----------------------------
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# -----------------------------
# Venue API
# -----------------------------
class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


# -----------------------------
# Transaction API
# -----------------------------
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("-timestamp")
    serializer_class = TransactionSerializer


# -----------------------------
# Transaction Item API
# -----------------------------
class TransactionItemViewSet(viewsets.ModelViewSet):
    queryset = TransactionItem.objects.all()
    serializer_class = TransactionItemSerializer

    def perform_create(self, serializer):
        transaction = Transaction.objects.latest("transaction_id")
        serializer.save(transaction=transaction)


# -----------------------------
# Dashboard APIs
# -----------------------------
@api_view(["GET"])
def venue_sales(request):
    data = (
        Transaction.objects
        .values("venue__name")
        .annotate(total_sales=Sum("total"))
        .order_by("venue__name")
    )
    return Response(data)


@api_view(["GET"])
def top_items(request):
    data = (
        TransactionItem.objects
        .values("item__name")
        .annotate(total_sold=Sum("qty"))
        .order_by("-total_sold")[:5]
    )
    return Response(data)