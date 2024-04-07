from django.db import models

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('Heart Doctor', 'Heart Doctor'),
        ('Surgeon', 'Surgeon'),
        ('Neurologist', 'Neurologist'),
        # Add more choices as needed
    ]
    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  # Assuming a standard phone number length
    experience_years = models.PositiveIntegerField()
    pin = models.CharField(max_length=10, default='0000')  # Add pin field with a default value

    def __str__(self):
        return self.name
