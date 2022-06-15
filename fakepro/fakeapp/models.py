from django.db import models

# Create your models here.
class Salesman(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=50)
    
