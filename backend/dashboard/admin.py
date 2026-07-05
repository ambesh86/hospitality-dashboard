from django.contrib import admin
from .models import Transaction, TransactionItem, Item, Venue

admin.site.register(Transaction)
admin.site.register(TransactionItem)
admin.site.register(Item)
admin.site.register(Venue)

