from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class HighSalaryEmployee(Employee):

    class Meta:
        proxy = True
        ordering = ['-salary']

    def high_salary(self):
        return self.salary > 50000