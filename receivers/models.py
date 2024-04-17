from django.db import models

class Receiver(models.Model):
    name = models.CharField(max_length=100, null=True)  
    surname = models.CharField(max_length=100, null=True)  
    age = models.PositiveIntegerField(null=True)  
    email = models.EmailField(null=True)  
    phone_number = models.CharField(max_length=15, null=True) 
    location = models.CharField(max_length=100, null=True)  
    blood_group = models.CharField(max_length=5, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], null=True)   

    def __str__(self):
        return self.name
