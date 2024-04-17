
from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from .models import Donor

class DonorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'surname', 'age', 'email', 'phone_number', 'blood_group', 'health_history', 'last_donation_date','location']
        widgets = {
            'last_donation_date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise ValidationError("You must be 18 or older to donate.")
        return age

    def clean_health_history(self):
        health_history = self.cleaned_data['health_history']
        if health_history != 'None':
            raise ValidationError("You cannot donate if you have a medical history.")
        return health_history


    def clean_last_donation_date(self):
        last_donation_date = self.cleaned_data['last_donation_date']
        if last_donation_date and last_donation_date > now().date():
            raise ValidationError("Last donation date cannot be in the future.")
        return last_donation_date
    
    def __init__(self, *args, **kwargs):
        super(DonorRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['location'] = forms.ChoiceField(choices=self.get_location_choices())

    def get_location_choices(self):
        # You can populate location choices dynamically here, for now, I'll provide static choices
        return [
            ('Location 1', 'Location 1'),
            ('Location 2', 'Location 2'),
            ('Location 3', 'Location 3'),
            # Add more choices as needed
        ]
