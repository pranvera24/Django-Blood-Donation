from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorRegistrationForm


from django.shortcuts import redirect

def doctor_registration(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/main/')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctors/doctor_login.html', {'form': form})





# def doctor_login(request):
#     if request.method == 'POST':
#         # if 'register' in request.POST:
#             form = DoctorRegistrationForm(request.POST)
#             if form.is_valid():
#                 user = form.save()

#                 # Create User object
#                 # user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

#                 # # Create Doctor object
#                 # Doctor.objects.create(
#                 #     user=user,
#                 #     name=form.cleaned_data['name'],
#                 #     surname=form.cleaned_data['surname'],
#                 #     email=form.cleaned_data['email'],
#                 #     phone_number=form.cleaned_data['phone_number'],
#                 #     experience_years=form.cleaned_data['experience_years'],
#                 #     specialization=form.cleaned_data['specialization']
#                 # )
#                 # form.save()
                

#                 return redirect('login_success')  # Redirect to a success page after registration
#         else:
#             # Handle doctor login form submission
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 # Check if the user is a doctor
#                 if hasattr(user, 'doctor'):
#                     login(request, user)
#                     return redirect('doctor_dashboard')  # Redirect to doctor dashboard
#                 else:
#                     # Handle case where authenticated user is not a doctor
#                     return render(request, 'doctors/doctor_login.html', {'error_message': 'You are not a registered doctor.'})
#             else:
#                 # Handle invalid login credentials
#                 return render(request, 'doctors/doctor_login.html', {'error_message': 'Invalid username or password.'})
#     else:
#         form = DoctorRegistrationForm()
#     return render(request, 'doctors/doctor_login.html', {'form': form})
