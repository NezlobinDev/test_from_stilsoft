from django.urls import include, path

from rest_framework.routers import DefaultRouter

from billing.api.views import TransactionViewSet, TransactionListViewSet


router = DefaultRouter()
router.register('', TransactionViewSet, basename='transaction')
router.register('list', TransactionListViewSet, basename='transaction_list')

urlpatterns = [
    path('', include(router.urls)),
]
