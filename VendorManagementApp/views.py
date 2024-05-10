from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import HistoricalPerformanceModel, PurchaseOrderModel, VendorModel
from .serializer import (HistoricalPerformanceSerializer,
                         PurchaseOrderSerializer, VendorSerializer)


class VendorViewSet(viewsets.ModelViewSet):
    queryset = VendorModel.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderSerializer

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformanceModel.objects.all()
    serializer_class = HistoricalPerformanceSerializer

@api_view(['GET', 'POST'])
def vendor_list(request):
    if request.method == 'GET':
        vendors = VendorModel.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vendor_detail(request, pk):
    vendor = get_object_or_404(VendorModel, pk=pk)

    if request.method == 'GET':
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
