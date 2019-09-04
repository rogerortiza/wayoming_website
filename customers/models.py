from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Customer(models.Model):
    CUSTOMERS_TYPE = (
        ("Active", "Active"),
        ("Inactive", "Inactive")
    )


    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False, blank=True)
    last_name = models.CharField(max_length=50, null=False, blank=True)
    other_names = models.CharField(max_length=50, default=" ")
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=30, null=False, blank=True)
    balance = models.IntegerField(default="0")
    customer_status = models.CharField(max_length=100, choices=CUSTOMERS_TYPE, default="Active")
    address = models.CharField(max_length=50, null=False, blank=False)

    def save(self, *args, **kwargs):
        return super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return "{}:{}".format(self.first_name, self.last_name)
