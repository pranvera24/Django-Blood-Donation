from django.shortcuts import render, redirect
from .models import Login
from .forms import DoctorRegistrationForm


from django.shortcuts import redirect

def login_page(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/main/')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'loginpage/login_page.html', {'form': form})
