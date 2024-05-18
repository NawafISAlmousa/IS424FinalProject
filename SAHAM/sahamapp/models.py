from django.db import models
from django.core.validators import MinLengthValidator # This function makes sure the data field is not less than a number we specify

class Customer(models.Model):
    userName = models.CharField(max_length=32,primary_key=True, validators=[MinLengthValidator(3)])
    password = models.CharField(max_length=32, validators=[MinLengthValidator(6)])

class Freelancer(models.Model):
    freelancerId = models.CharField(max_length=32,primary_key=True, validators=[MinLengthValidator(3)])
    password = models.CharField(max_length=32, validators=[MinLengthValidator(6)])
    description = models.CharField(max_length=500)
    name = models.CharField(max_length=32, validators=[MinLengthValidator(3)])
    phonenumber = models.CharField(max_length=10, validators=[MinLengthValidator()])

