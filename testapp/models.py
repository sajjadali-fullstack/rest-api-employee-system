from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.IntegerField() 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)  #EG:- IT Department
    designation = models.CharField(max_length=99)  # Junior Developer
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    joining_date = models.DateField()
    City = models.CharField(max_length=55)
    Address = models.CharField(max_length=400)
