from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100, null=True)  # Allow null values for user input
    surname = models.CharField(max_length=100, null=True)  # Allow null values for user input
    age = models.PositiveIntegerField(null=True)  # Allow null values for user input
    email = models.EmailField(null=True)  # Allow null values for user input
    phone_number = models.CharField(max_length=15, null=True)  # Allow null values for user input
    blood_group = models.CharField(max_length=5, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], null=True)  # Allow null values for user input
    HEALTH_CHOICES = [
        ('None', 'None'),
        ('Hypertension', 'Hypertension'),
        ('Diabetes', 'Diabetes'),
        ('Asthma', 'Asthma'),
        ('Heart Disease', 'Heart Disease'),
        ('Other', 'Other')
    ]
    health_history = models.CharField(max_length=50, choices=HEALTH_CHOICES, null=True)  # Allow null values for user input
    last_donation_date = models.DateField(null=True, blank=True)  # Allow null values for user input

    def __str__(self):
        return self.name
