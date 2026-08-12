from rest_framework import serializers
from .models import Product
from .models import Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =[
            'name',
            'description',
            'price',
            'image',
            'brand',
            'category',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields =[
            'id',
            'name',
            'slug',
        ]