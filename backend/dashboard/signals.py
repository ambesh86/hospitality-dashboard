from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .serializers import TransactionSerializer

@receiver(post_save, sender=Transaction)
def broadcast_transaction(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        data = TransactionSerializer(instance).data
        async_to_sync(channel_layer.group_send)(
            "dashboard",
            {
                "type": "send_transaction_update",
                "data": data,
            }
        )
