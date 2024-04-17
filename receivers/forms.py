from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from .models import Receiver

class ReceiverRegistrationForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = ['name', 'surname', 'age', 'email', 'phone_number', 'blood_group','location']

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise ValidationError("You must be 18 or older to donate.")
        return age


    
    def __init__(self, *args, **kwargs):
        super(ReceiverRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['location'] = forms.ChoiceField(choices=self.get_location_choices())

    def get_location_choices(self):
        # You can populate location choices dynamically here, for now, I'll provide static choices
        return [
            ('Location 1', 'Location 1'),
            ('Location 2', 'Location 2'),
            ('Location 3', 'Location 3'),
            # Add more choices as needed
        ]
