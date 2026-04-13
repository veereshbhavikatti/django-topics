from django.db import models

# Create your models here.
class Person(models.Model):
    name= models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100)
    datr_of_birth= models.DateField()

    class meta:
        abstract=True

    def __str__(self):
        return super.name
    
class Employee(Person):
    employee_id = models.CharField(max_length=100, unique=True)  
    position = models.CharField(max_length=200)
    hire_date = models.DateField()

class Customer(Person):
    customer_id = models.CharField(max_length=100, unique=True)  
    join_date = models.DateField()

class EmployeeProxy(Employee):
    class meta:
        proxy=True
        ordering =['name']

    def is_senior(self):
        from datetime import date
        return (date.today()- self.hire_date).days > 5 * 365
    


class CustomerProxy(Customer):
    class meta:
        proxy=True
        ordering =['join_date']

    def is_loyal(self):
        from datetime import date
        return (date.today()- self.join_date_date).days > 3 * 365