from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100, null=True)  
    surname = models.CharField(max_length=100, null=True)  
    age = models.PositiveIntegerField(null=True)  
    email = models.EmailField(null=True)  
    phone_number = models.CharField(max_length=15, null=True) 
    location = models.CharField(max_length=100, null=True)  
    blood_group = models.CharField(max_length=5, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], null=True)  # Allow null values for user input
    HEALTH_CHOICES = [
        ('None', 'None'),
        ('Hypertension', 'Hypertension'),
        ('Diabetes', 'Diabetes'),
        ('Asthma', 'Asthma'),
        ('Heart Disease', 'Heart Disease'),
        ('Other', 'Other')
    ]
    health_history = models.CharField(max_length=50, choices=HEALTH_CHOICES, null=True)  
    last_donation_date = models.DateField(null=True, blank=True)  

    def __str__(self):
        return self.name
