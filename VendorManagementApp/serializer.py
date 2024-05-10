from rest_framework import serializers

from .models import HistoricalPerformanceModel, PurchaseOrderModel, VendorModel


class VendorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = VendorModel
        fields = "__all__"

class PurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PurchaseOrderModel
        fields = "__all__"

class HistoricalPerformanceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = HistoricalPerformanceModel
        fields = "__all__"