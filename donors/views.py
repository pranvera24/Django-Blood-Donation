from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Donor
from .forms import DonorRegistrationForm


def donor_registration(request):
    if  request.method == 'POST':
        form = DonorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form is valid. Data saved successfully")
            return redirect ('/')
        else:
            print(form.errors)
    else:
        form = DonorRegistrationForm()
    return render (request,'donors/donor_login.html' , {'form':form})

