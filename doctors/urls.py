# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login/', views.doctor_registration, name='doctor_login'),
#     # Add more URL patterns for doctor-related views as needed
# ]



from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.doctor_registration, name='doctor_login'),
    path('profile/<str:doctor_pin>/', views.doctor_profile, name='doctor_profile'),
    # Add more URL patterns for doctor-related views as needed
]

