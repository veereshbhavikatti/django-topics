from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.student.name