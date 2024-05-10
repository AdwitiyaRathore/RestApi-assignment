from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'vendors', views.VendorViewSet)
router.register(r'purchase-orders', views.PurchaseOrderViewSet)
router.register(r'historical-performance', views.HistoricalPerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vendors/', views.vendor_list),
    path('vendors/<int:pk>/', views.vendor_detail),
]
