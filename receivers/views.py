from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Receiver
from .forms import ReceiverRegistrationForm


def receiver_registration(request):
    if  request.method == 'POST':
        form = ReceiverRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form is valid. Data saved successfully")
            return redirect ('/')
        else:
            print(form.errors)
    else:
        form = ReceiverRegistrationForm()
    return render (request,'receivers/receiver_login.html' , {'form':form})

