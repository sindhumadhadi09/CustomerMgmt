import datetime

from django.db import models
from django.utils import timezone

class Customer(models.Model):
    customer_firstname = models.CharField(max_length=200)
    customer_lastname = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=200)
    customer_city = models.CharField(max_length=200)
    customer_zipcode = models.CharField(max_length=200)
    customer_state = models.CharField(max_length=200)
    def __str__(self):
        return self.lastname
