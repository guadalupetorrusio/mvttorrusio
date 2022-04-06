from django.db import models

class Person(models.Model):
    name= models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    date_birth = models.DateField()
    