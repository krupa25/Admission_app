from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.TextField(max_length=200)
    gender = models.CharField(max_length=255)
    hobbies = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    dob = models.DateField()
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)