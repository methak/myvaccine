from django.db import models
from django.urls import reverse

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    appointment = models.BooleanField()
    walkin = models.BooleanField()
    hours = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'provider_id': self.id})