from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import FoodType, FoodItem, UserOrder
from .serializers import FoodTypeSerializer, FoodItemSerializer, UserOrderSerializer

from rest_framework import generics, permissions, status, serializers
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import FoodType, FoodItem, Cart
from .serializers import FoodTypeSerializer, FoodItemSerializer, CartSerializer, UserSerializer

class RegisterView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = (permissions.AllowAny,)


class FoodItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = (permissions.IsAdminUser,)

class FoodItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = (permissions.IsAdminUser,)

class CartAddAPIView(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart = serializer.save()
        return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)

class UserOrderListAPIView(generics.ListAPIView):
    serializer_class = UserOrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return UserOrder.objects.filter(user=self.request.user)
class OrderCreateAPIView(generics.CreateAPIView):
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user_cart = Cart.objects.filter(user=self.request.user)
        items = [cart.food_item for cart in user_cart]
        serializer.save(user=self.request.user, items=items)
        user_cart.delete()

