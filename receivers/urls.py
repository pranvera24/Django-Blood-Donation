from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.receiver_login, name='receiver_login'),
    # Add more URL patterns for receiver-related views as needed
]
