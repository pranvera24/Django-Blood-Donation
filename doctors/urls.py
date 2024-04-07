from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.doctor_registration, name='doctor_login'),
    # Add more URL patterns for doctor-related views as needed
]
