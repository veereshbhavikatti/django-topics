from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    country =models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    punlished_date = models.DateField()

    def __str__(self):
        return self.title
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    Customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"oder {self.id}"
    
class Orderitem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    book =models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def total_price(self):
        return self.quantity * self.book.price