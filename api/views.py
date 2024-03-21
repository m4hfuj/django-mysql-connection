from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
from base.models import Customer, Product, Order
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer


@api_view(['GET', 'POST'])
def customer_view(request):
    if request.method == 'GET':
        entries = Customer.objects.all()
        serializer = CustomerSerializer(entries, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Entry created successfully"}, status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def product_view(request):
    if request.method == 'GET':
        entries = Product.objects.all()
        serializer = ProductSerializer(entries, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Entry created successfully"}, status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def order_view(request):
    if request.method == 'GET':
        entries = Order.objects.all()
        serializer = OrderSerializer(entries, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Entry created successfully"}, status.HTTP_201_CREATED)


