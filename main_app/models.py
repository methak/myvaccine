from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    appointment = models.BooleanField()
    walkin = models.BooleanField()
    hours = models.CharField(max_length=100)
    vaccines = models.ManyToManyField(Vaccine)

    def __str__(self):
        return self.name
    
    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'provider_id': self.id})

class VaccineCard(models.Model):
    date = models.DateField('appointment date',default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    gotvaccine = models.BooleanField(default=False)
    def __str__(self):
        return self.provider
    class Meta:
        ordering = ['-date']

    