from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.donor_registration, name='donor_register'),
    # Add more URL patterns for donor-related views as needed
]
