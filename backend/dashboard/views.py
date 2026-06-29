from rest_framework import viewsets
from .models import Transaction,Venue,TransactionItem
from .serializers import TransactionSerializer,VenueSerializer,TransactionItemSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("-timestamp")
    serializer_class = TransactionSerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = TransactionItem.objects.all()
    serializer_class = TransactionItemSerializer
