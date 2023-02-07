from django.db import models

# Create your models here.
class student(models.Model):
    nim = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.IntegerField()