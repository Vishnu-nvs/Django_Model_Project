from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    Cust_Id=models.PositiveIntegerField()
    email=models.EmailField()
    date_of_join=models.DateField()
    salary=models.FloatField()

