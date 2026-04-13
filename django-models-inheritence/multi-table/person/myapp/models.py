from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Employee(Person):
    salary = models.IntegerField()
    department = models.CharField(max_length=100)
