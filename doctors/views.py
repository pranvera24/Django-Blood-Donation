# from django.shortcuts import render, redirect
# from .models import Doctor
# from .forms import DoctorRegistrationForm


# from django.shortcuts import redirect

# def doctor_registration(request):
#     if request.method == 'POST':
#         form = DoctorRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/main/')
#     else:
#         form = DoctorRegistrationForm()
#     return render(request, 'doctors/doctor_login.html', {'form': form})


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Doctor
# from .forms import DoctorRegistrationForm

# def doctor_registration(request):
#     if request.method == 'POST':
#         form = DoctorRegistrationForm(request.POST)
#         if form.is_valid():
#             doctor = form.save()
#             return redirect('doctor_profile', doctor_pin=doctor.pin)
#     else:
#         form = DoctorRegistrationForm()
#     return render(request, 'doctors/doctor_login.html', {'form': form})

# def doctor_profile(request, doctor_pin):
#     doctor = get_object_or_404(Doctor, pin=doctor_pin)
#     return render(request, 'profile.html', {'doctor': doctor})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from .forms import DoctorRegistrationForm
from donors.models import Donor
from receivers.models import Receiver
from receivers.forms import ReceiverRegistrationForm

def doctor_registration(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            doctor = form.save()
            return redirect('doctor_profile', doctor_pin=doctor.pin)
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctors/doctor_login.html', {'form': form})

def doctor_profile(request, doctor_pin):
    doctor = get_object_or_404(Doctor, pin=doctor_pin)
    donors_list = Donor.objects.all()
    receivers_list = Receiver.objects.all()
    return render(request, 'profile.html', {'doctor': doctor, 'donors_list': donors_list, 'receivers_list': receivers_list})
