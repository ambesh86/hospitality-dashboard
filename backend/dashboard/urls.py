from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VenueViewSet, ItemViewSet, TransactionViewSet, venue_sales, top_items

router = DefaultRouter()
router.register(r'venues', VenueViewSet)
router.register(r'items', ItemViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

custom_urlpatterns = [
    path('transactions/venue-sales/', venue_sales),
    path('transactions/top-items/', top_items),
]

urlpatterns = [
    path('', include(router.urls)),
] + custom_urlpatterns