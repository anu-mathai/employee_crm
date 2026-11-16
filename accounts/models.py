from django.db import models

# Create your models here.
class Employee(models.Model):

    name = models.CharField(max_length=200)

    email = models.EmailField(unique=True)

    department = models.CharField(max_length=200) 

    salary = models.DecimalField(max_digits=8,decimal_places=2)

    location = models.CharField(max_length=200) 