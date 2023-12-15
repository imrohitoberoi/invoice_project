from rest_framework import serializers
from . import models

class InvoiceItemSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        super(InvoiceItemSerializer).validate(attrs)
        data = attrs['context'].request.data
        if data['amount'] <= 0:
            raise serializers.ValidationError('Invoice item amount must be a positive value')
        if data['quantity'] <= 0:
            raise serializers.ValidationError('Invoice item quantity must be a positive value')
        if data['price'] <= 0:
            raise serializers.ValidationError('Invoice item price must be a positive value')
        if data['amount'] != data['quantity'] * data['price']:
            raise serializers.ValidationError('Invoice item amount mismatched')
        return data

    class Meta:
        model = models.InvoiceItem
        fields = '__all__'


class InvoiceBillSundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceBillSundry
        fields = '__all__'


class InvoiceHeaderSerializer(serializers.ModelSerializer):
    invoice_item = InvoiceItemSerializer(many=True)
    invoice_bill_sundry = InvoiceBillSundrySerializer(many=True)

    # def validate(self, attrs):
    #     data = attrs['context'].request.data

    #     return data

    class Meta:
        model = models.InvoiceHeader
        fields = [
            'id', 'date', 'invoice_number', 'customer_name', 'billing_address', 'shipping_address', 'gst_in',
            'total_amount', 'invoice_item', 'invoice_bill_sundry'
        ]
