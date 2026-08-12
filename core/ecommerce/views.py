from django.contrib.gis import serializers
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required,user_passes_test
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Product,Category
from .forms import ContactForm
from .serializers import ProductSerializer
from .serializers import CategorySerializer



def home(request):
    context={
        "customer_name":"Surajan shrestha",
        "product_count":"12",
    }
    return render(request, "ecommerce/index.html",context)

def about(request):
    return render(request, "ecommerce/about.html")   

def contact(request):
    Form=ContactForm()
    return render(request, "ecommerce/contact.html",{"form":ContactForm})

def collection(request):
    products=Product.objects.all()
    return render(request,"ecommerce/collection.html",{"products": products})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ecommerce:login')
    else:
        form = UserCreationForm()
    return render(request, 'ecommerce/register.html', {'form': form})

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ecommerce:profile')
        else:
            error_message = "Invalid username or password."
    return render(request, 'ecommerce/login.html', {'error_message': error_message})


@login_required
def profile(request):
    return render(request, 'ecommerce/profile.html')

@login_required
@require_POST
def logout_view(request):
    logout(request)
    return redirect('ecommerce:home')

@login_required
def cart(request):
    return render(request, 'ecommerce/cart.html')

class HelloAPIView(APIView):
    def get(self, request):
        return Response(
            {"message": "Hello, World!"}, 
            status=status.HTTP_200_OK)

class ProductListAPIView(APIView):
    def get(self ,request):
        products=Product.objects.all()
        serializer=ProductSerializer(
            products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


class CategoryDetailsAPIView(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        category=self.get_object(pk)
        serializer=CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,pk):
        category=self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

