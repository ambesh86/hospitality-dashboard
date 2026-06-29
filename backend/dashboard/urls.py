from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VenueViewSet, ItemViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'venues', VenueViewSet)
router.register(r'items', ItemViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]