from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        order = Order(user=user, product_id=data['product_id'], quantity=data['quantity'])
        order.save()
        return Response({'message': 'Item added to cart'})

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
