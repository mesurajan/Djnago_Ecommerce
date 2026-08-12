from django.urls import path
from .views import (ProductListAPIView, HelloAPIView,ProductDetailAPIView,CategoryDetailsAPIView)

urlpatterns = [
    path('hello/', HelloAPIView.as_view(), name='hello'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('categories/',CategoryDetailsAPIView.as_view(),name='category-view'),
    path('categories/<int:pk>/',CategoryDetailsAPIView.as_view(),name='category-detail'),
    
]
   