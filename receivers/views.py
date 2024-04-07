from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Receiver

def receiver_login(request):
    if request.method == 'POST':
        # Handle receiver login form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # Check if the user is a receiver
            if hasattr(user, 'receiver'):
                login(request, user)
                return redirect('receiver_dashboard')  # Redirect to receiver dashboard
    return render(request, 'receiver_login.html')
