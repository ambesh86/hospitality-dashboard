from rest_framework import serializers
from .models import Venue, Transaction, TransactionItem,Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "price"]

class TransactionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionItem
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    items = TransactionItemSerializer(many=True)

    class Meta:
        model = Transaction
        fields = ["venue", "transaction_id", "timestamp", "type", "total", "staff_id", "items"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        transaction = Transaction.objects.create(**validated_data)
        for item in items_data:
            TransactionItem.objects.create(transaction=transaction, **item)
        return transaction

    

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ["id", "name", "location"]



