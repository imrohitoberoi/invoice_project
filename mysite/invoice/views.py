from django.shortcuts import get_object_or_404
from . import serializers
from rest_framework import viewsets
from rest_framework.response import Response

class InvoiceViewSet(viewsets.ViewSet):
    """
    A ViewSet for CRUD operations on invoice.
    """
    serializer_class = serializers.InvoiceHeaderSerializer
    model = 
