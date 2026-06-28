# Create your models here.
from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    SALE = "sale"
    VOID = "void"
    REFUND = "refund"
    TYPE_CHOICES = [
        (SALE, "Sale"),
        (VOID, "Void"),
        (REFUND, "Refund"),
    ]

    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name="transactions")
    transaction_id = models.CharField(max_length=100, unique=True)
    timestamp = models.DateTimeField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    staff_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.venue.name} - {self.transaction_id}"


class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="items")
    item_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} x {self.qty}"
