from django.db import models


# Create your models here.
class VendorModel(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField(max_length=10, primary_key=True)
    address = models.TextField()
    vendor_code = models.CharField(max_length=20)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.name
    
class PurchaseOrderModel(models.Model):
    po_number = models.CharField(max_length=20)
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quality = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

    def __str__(self):
        return self.po_number
    
class HistoricalPerformanceModel(models.Model):
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()