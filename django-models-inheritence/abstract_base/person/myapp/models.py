from django.db import models

# Create your models here.
class Person(models.Model):
    name= models.CharField(max_length=200)
    age=models.IntegerField()

    class meta:
        abstract =True

class Employee (Person):
    salary =models.IntegerField()
    department=models.CharField(max_length=100)

class Student(Person):
    course = models.CharField(max_length=100)
    marks = models.IntegerField()
