from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Customer, Product, Order
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
