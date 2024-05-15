from django import forms
from doctors.models import Doctor
from doctors.forms import DoctorRegistrationForm
from donors.forms import DonorRegistrationForm
from receivers.forms import ReceiverRegistrationForm

# class DoctorRegistrationForm(forms.ModelForm):
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#     email = forms.EmailField()
#     experience_years = forms.IntegerField()
#     pin = forms.CharField(max_length=10)  

#     class Meta:
#         model = Doctor
#         fields = ['specialization', 'name', 'surname', 'email', 'phone_number', 'experience_years', 'password', 'pin']

#     def clean_pin(self):
#         pin = self.cleaned_data.get('pin')
#         # list of valid pins 
#         valid_pins = ['123', '456', '789']  
#         if pin not in valid_pins:
#             raise forms.ValidationError("Invalid PIN")
#         return pin
