from django.db import models

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    appointment = models.BooleanField()
    walkin = models.BooleanField()
    hours = models.CharField(max_length=100)