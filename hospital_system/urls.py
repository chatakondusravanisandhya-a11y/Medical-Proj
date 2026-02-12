from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'hospital_system'

urlpatterns = [
    # Landing and main pages
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    # Departments
    path('departments/', views.departments, name='departments'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    
    # Doctors
    path('doctors/', views.doctors, name='doctors'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    
    # Services
    path('services/', views.services, name='services'),
    
    # Appointments
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('appointment/<int:pk>/', views.appointment_confirmation, name='appointment_confirmation'),
    
    # Cost Estimate
    path('cost-estimate/', views.cost_estimate, name='cost_estimate'),
    
    # AJAX endpoints
    path('api/doctors-by-department/<int:dept_id>/', views.get_doctors_by_department, name='get_doctors_by_department'),
    path('api/available-slots/', views.get_available_slots, name='get_available_slots'),

    # Authentication
    path('accounts/login/', views.login_user, name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='hospital_system:landing'), name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('profile/update/', views.update_profile, name='update_profile'),
]
