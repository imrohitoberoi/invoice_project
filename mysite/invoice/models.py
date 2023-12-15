from django.db import models


class InvoiceHeader(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    invoice_number = models.AutoField(unique=True)
    customer_name = models.CharField(max_length=128)
    billing_address = models.CharField(max_length=256)
    shipping_address = models.CharField(max_length=256)
    gst_in = models.CharField(max_length=128)
    total_amount = models.FloatField()


class InvoiceItem(models.Model):
    quantity = models.FloatField()
    price = models.FloatField()
    amount = models.FloatField()
    invoice = models.ForeignKey(InvoiceHeader, on_delete=models.CASCADE)


class InvoiceBillSundry(models.Model):
    bill_sundry_name = models.CharField(max_length=128)
    amount = models.FloatField()
    invoice = models.ForeignKey(InvoiceHeader, on_delete=models.CASCADE)
