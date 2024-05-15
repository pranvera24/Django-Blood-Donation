
# from django.shortcuts import render, redirect
# from .forms import DoctorRegistrationForm, DonorRegistrationForm, ReceiverRegistrationForm

# def login_page(request):
#     doctor_form = DoctorRegistrationForm(request.POST or None)
#     donor_form = DonorRegistrationForm(request.POST or None)
#     receiver_form = ReceiverRegistrationForm(request.POST or None)

#     if request.method == 'POST':
#         login_type = request.POST.get('login_type')
#         if login_type == 'doctor':
#             form = doctor_form
#         elif login_type == 'donor':
#             form = donor_form
#         elif login_type == 'receiver':
#             form = receiver_form
#         else:
#             # Handle invalid login type here
#             return redirect('/login/')  # Redirect to login page again or show an error
#         if form.is_valid():
#             form.save()
#             return redirect('/main/')  # Redirect to main page after successful login

#     return render(request, 'loginpage/login_page.html', {'doctor_form': doctor_form, 'donor_form': donor_form, 'receiver_form': receiver_form})

from django.shortcuts import render, redirect
from .forms import DoctorRegistrationForm, DonorRegistrationForm, ReceiverRegistrationForm
from doctors.models import Doctor

def login_page(request):
    if request.method == 'POST':
        login_type = request.POST.get('login_type')
        if login_type == 'doctor':
            doctor_form = DoctorRegistrationForm(request.POST)
            if doctor_form.is_valid():
                doctor_email = doctor_form.cleaned_data['email']
                # Check if the doctor exists
                if Doctor.objects.filter(email=doctor_email).exists():
                    return redirect('/main/')  # Redirect to main page if doctor exists
                else:
                    return redirect('/')  # Redirect to root if doctor does not exist
        elif login_type == 'donor':
            donor_form = DonorRegistrationForm(request.POST)
            if donor_form.is_valid():
                donor_form.save()
                return redirect('/main/')  # Redirect to main page after successful login
        elif login_type == 'receiver':
            receiver_form = ReceiverRegistrationForm(request.POST)
            if receiver_form.is_valid():
                receiver_form.save()
                return redirect('/main/')  # Redirect to main page after successful login
    else:
        doctor_form = DoctorRegistrationForm()
        donor_form = DonorRegistrationForm()
        receiver_form = ReceiverRegistrationForm()

    return render(request, 'loginpage/login_page.html', {'doctor_form': doctor_form, 'donor_form': donor_form, 'receiver_form': receiver_form})
