from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(unique=True)

    def __str__(self):
        return self.name
    
class Address(models.Model):
    customer= models.OneToOneField(customer, on_delete=models.CASCADE)
    street= models.CharField(max_length=255)
    City =models.CharField(max_length=200)
    state= models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def  __str__(self):
        return f"(self.street), {self.city}"
    
class catrgory(models.Model):
    name = models.CharField(max_length=200 ,unique=True)
   

    def __str__(self):
        return self.name
    
class product(models.Model):
    name = models.CharField(max_length=200 ,unique=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    category= models.ForeignKey(customer, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
    
class order(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    products= models.ManyToManyField(product, related_name='orders')
    order_data=models.DateTimeField(auto_now_add=True)
    total_price= models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def calculate_total_price(self):
        self.total_price=sum(self.product.price for product in self.product.all())
        self.save()

    def __str__(self):
        return f"order by {self.id} by {self.customer.name}"