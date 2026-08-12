from django.db import models

class Product(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00,blank=True,null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    brand=models.ForeignKey('Brand', on_delete=models.CASCADE, blank=True, null=True)   
    category=models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo= models.ImageField(upload_to='brands/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)

    def __str__(self):
        return self.name

class Customer(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    age= models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    count = models.IntegerField(default=1,blank=True,null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00,blank=True,null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.first_name} {self.customer.last_name}"


    