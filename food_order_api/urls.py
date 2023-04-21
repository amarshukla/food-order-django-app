from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
            FoodTypeListCreateAPIView, CartAddAPIView, OrderCreateAPIView,
            UserOrderListAPIView, RegisterView, FoodItemListCreateAPIView,
            FoodItemDetailAPIView
)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('food-types/', FoodTypeListCreateAPIView.as_view(), name='food_types_list_create'),
    path('food-items/', FoodItemListCreateAPIView.as_view(), name='food-item-list-create'),
    path('food-items/<int:pk>/', FoodItemDetailAPIView.as_view(), name='food-item-detail'),
    path('add-to-cart/', CartAddAPIView.as_view(), name='add_to_cart'),
    path('place-order/', OrderCreateAPIView.as_view(), name='place_order'),
    path('my-orders/', UserOrderListAPIView.as_view(), name='my_orders'),
]
