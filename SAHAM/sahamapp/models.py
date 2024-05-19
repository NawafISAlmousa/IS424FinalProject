from django.db import models
from django.core.validators import MinLengthValidator # This function makes sure the data field is not less than a number we specify



class Freelancer(models.Model):
    freelancerId = models.CharField(max_length=6,primary_key=True)
    email = models.EmailField(max_length=256,unique=True)
    password = models.CharField(max_length=32, validators=[MinLengthValidator(6)])
    description = models.CharField(max_length=500)
    name = models.CharField(max_length=32, validators=[MinLengthValidator(3)])
    phonenumber = models.CharField(max_length=10, validators=[MinLengthValidator(10)])


class Service(models.Model):
    serviceId = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=32, validators=[MinLengthValidator(3)])
    description = models.CharField(max_length=500)
    price = models.FloatField()
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE, related_name='services')


class Customer(models.Model): # 
    userName = models.CharField(max_length=32,primary_key=True, validators=[MinLengthValidator(3)])
    password = models.CharField(max_length=32, validators=[MinLengthValidator(6)])
    bookedServices = models.ManyToManyField(Service, blank=True, related_name="customers")