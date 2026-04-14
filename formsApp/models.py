from django.db import models

# Create your models here.

# (models.Model)  - inheritance in python, this class extends to models
class Login(models.Model):
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=100)
        #self is refers to the class
    def __str__(self):
        return self.email;