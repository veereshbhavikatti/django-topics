from django.db import models

# Create your models here.
class FormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    attachment = models.FileField(upload_to="attachments/")