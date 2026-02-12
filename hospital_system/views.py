from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.db.models import Q
from datetime import datetime, timedelta
from .models import (
    Hospital, Department, Doctor, Patient, Appointment, 
    Service, Infrastructure, Testimonial
)
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


# Landing Page (Public)
def landing(request):
    """Landing page with login and registration for public visitors"""
    if request.user.is_authenticated:
        return redirect('hospital_system:home')
    
    hospital = Hospital.objects.first()
    context = {
        'hospital': hospital,
    }
    return render(request, 'landing.html', context)


# Custom Login View for Landing Page
def login_user(request):
    """Handle user login from landing page"""
    if request.user.is_authenticated:
        return redirect('hospital_system:home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('hospital_system:home')
        else:
            return render(request, 'landing.html', {
                'hospital': Hospital.objects.first(),
                'error': 'Invalid username or password',
            })
    
    return redirect('hospital_system:landing')


# Home View
@login_required(login_url='hospital_system:landing')
def home(request):
    """Home page with hospital info and departments - requires login"""
    hospital = Hospital.objects.first()
    departments = Department.objects.all()
    infrastructure = Infrastructure.objects.all()
    testimonials = Testimonial.objects.filter(is_published=True)[:6]
    
    default_dept_image = 'https://images.unsplash.com/photo-1580281657526-3e6a4e8f2d56?auto=format&fit=crop&w=800&q=60'

    # Build a list of departments with images from model
    departments_with_images = []
    for d in departments:
        # Use department's image if available, otherwise use default
        img = d.image.url if d.image else default_dept_image
        departments_with_images.append({'dept': d, 'image': img})

    # Fallback doctor image (used when doctor.image is not provided)
    fallback_doctor_image = 'https://images.unsplash.com/photo-1607746882042-944635dfe10e?auto=format&fit=crop&w=800&q=60'

    context = {
        'hospital': hospital,
        'departments': departments,
        'departments_with_images': departments_with_images,
        'infrastructure': infrastructure,
        'testimonials': testimonials,
        'fallback_doctor_image': fallback_doctor_image,
    }
    return render(request, 'index.html', context)


# Services/Departments
def departments(request):
    """List all departments"""
    departments = Department.objects.all()
    default_dept_image = 'https://images.unsplash.com/photo-1580281657526-3e6a4e8f2d56?auto=format&fit=crop&w=800&q=60'
    departments_with_images = []
    for d in departments:
        # Use department's image if available, otherwise use default
        img = d.image.url if d.image else default_dept_image
        departments_with_images.append({'dept': d, 'image': img})
    return render(request, 'departments.html', {'departments_with_images': departments_with_images})


def department_detail(request, pk):
    """Department detail view with services and doctors"""
    department = get_object_or_404(Department, pk=pk)
    services = Service.objects.filter(department=department)
    doctors = Doctor.objects.filter(specialization=department)
    # Use department's image, default to unsplash
    default_dept_image = 'https://images.unsplash.com/photo-1580281657526-3e6a4e8f2d56?auto=format&fit=crop&w=800&q=60'
    dept_image = department.image.url if department.image else default_dept_image

    context = {
        'department': department,
        'services': services,
        'doctors': doctors,
        'dept_image': dept_image,
    }
    return render(request, 'department_detail.html', context)


# Doctors
def doctors(request):
    """List all doctors with filter option"""
    doctors = Doctor.objects.all()
    departments = Department.objects.all()
    
    # Filter by department
    dept_id = request.GET.get('department')
    if dept_id:
        doctors = doctors.filter(specialization_id=dept_id)
    
    # Search by name
    search = request.GET.get('search')
    if search:
        doctors = doctors.filter(
            Q(name__icontains=search) | 
            Q(qualification__icontains=search)
        )
    
    fallback_doctor_image = 'https://images.unsplash.com/photo-1607746882042-944635dfe10e?auto=format&fit=crop&w=800&q=60'
    context = {
        'doctors': doctors,
        'departments': departments,
        'selected_department': dept_id,
        'search': search,
        'fallback_doctor_image': fallback_doctor_image,
    }
    return render(request, 'doctors.html', context)


def doctor_detail(request, pk):
    """Doctor detail view"""
    doctor = get_object_or_404(Doctor, pk=pk)
    available_dates = _get_available_booking_dates()
    available_times = _get_available_booking_times()
    
    fallback_doctor_image = 'https://images.unsplash.com/photo-1607746882042-944635dfe10e?auto=format&fit=crop&w=800&q=60'
    context = {
        'doctor': doctor,
        'available_dates': available_dates,
        'available_times': available_times,
        'fallback_doctor_image': fallback_doctor_image,
    }
    return render(request, 'doctor_detail.html', context)


# Appointments
def book_appointment(request):
    """Book an appointment"""
    from django.db import IntegrityError
    # Prefill form from GET params (e.g., ?doctor=1&department=2)
    form_data = {}
    if request.method == 'GET':
        # prefill if query params provided
        q_doctor = request.GET.get('doctor')
        q_department = request.GET.get('department')
        q_date = request.GET.get('date')
        q_time = request.GET.get('time')
        if q_doctor:
            form_data['doctor_id'] = q_doctor
        if q_department:
            form_data['department_id'] = q_department
        if q_date:
            form_data['appointment_date'] = q_date
        if q_time:
            form_data['appointment_time'] = q_time

    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        patient_email = request.POST.get('patient_email')
        patient_phone = request.POST.get('patient_phone')
        doctor_id = request.POST.get('doctor')
        department_id = request.POST.get('department')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        reason = request.POST.get('reason')

        form_data = {
            'patient_name': patient_name,
            'patient_email': patient_email,
            'patient_phone': patient_phone,
            'doctor_id': doctor_id,
            'department_id': department_id,
            'appointment_date': appointment_date,
            'appointment_time': appointment_time,
            'reason': reason,
        }

        # Basic validation
        if not (patient_name and patient_email and patient_phone and doctor_id and department_id and appointment_date and appointment_time):
            return render(request, 'book_appointment.html', {
                'error': 'Please fill all required fields.',
                'departments': Department.objects.all(),
                'doctors': Doctor.objects.filter(is_available=True),
                'available_dates': _get_available_booking_dates(),
                'available_times': _get_available_booking_times(),
                'form_data': form_data,
            })

        # Parse date/time
        try:
            from datetime import datetime
            appt_date = datetime.strptime(appointment_date, '%Y-%m-%d').date()
            appt_time = datetime.strptime(appointment_time, '%H:%M').time()
        except Exception as e:
            return render(request, 'book_appointment.html', {
                'error': 'Invalid date or time format.',
                'departments': Department.objects.all(),
                'doctors': Doctor.objects.filter(is_available=True),
                'available_dates': _get_available_booking_dates(),
                'available_times': _get_available_booking_times(),
                'form_data': form_data,
            })

        try:
            appointment = Appointment.objects.create(
                patient_name=patient_name,
                patient_email=patient_email,
                patient_phone=patient_phone,
                doctor_id=doctor_id,
                department_id=department_id,
                appointment_date=appt_date,
                appointment_time=appt_time,
                reason=reason,
            )
            return redirect('hospital_system:appointment_confirmation', pk=appointment.pk)
        except IntegrityError:
            return render(request, 'book_appointment.html', {
                'error': 'Selected slot is already booked. Please choose another slot.',
                'departments': Department.objects.all(),
                'doctors': Doctor.objects.filter(is_available=True),
                'available_dates': _get_available_booking_dates(),
                'available_times': _get_available_booking_times(),
                'form_data': form_data,
            })
        except Exception as e:
            return render(request, 'book_appointment.html', {
                'error': str(e),
                'departments': Department.objects.all(),
                'doctors': Doctor.objects.filter(is_available=True),
                'available_dates': _get_available_booking_dates(),
                'available_times': _get_available_booking_times(),
                'form_data': form_data,
            })

    doctors = Doctor.objects.filter(is_available=True)
    departments = Department.objects.all()
    available_dates = _get_available_booking_dates()
    available_times = _get_available_booking_times()

    context = {
        'doctors': doctors,
        'departments': departments,
        'available_dates': available_dates,
        'available_times': available_times,
        'form_data': form_data,
    }
    return render(request, 'book_appointment.html', context)


def appointment_confirmation(request, pk):
    """Show appointment confirmation"""
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointment_confirmation.html', {'appointment': appointment})


# Contact
def contact(request):
    """Contact page"""
    hospital = Hospital.objects.first()
    
    if request.method == 'POST':
        # Handle contact form submission
        return render(request, 'contact_success.html', {
            'name': request.POST.get('name'),
        })
    
    return render(request, 'contact.html', {'hospital': hospital})


# About
def about(request):
    """About hospital page"""
    hospital = Hospital.objects.first()
    departments = Department.objects.all()
    
    context = {
        'hospital': hospital,
        'departments': departments,
    }
    return render(request, 'about.html', context)


# Services
def services(request):
    """All services page"""
    services = Service.objects.all()
    departments = Department.objects.all()
    
    dept_id = request.GET.get('department')
    if dept_id:
        services = services.filter(department_id=dept_id)
    
    context = {
        'services': services,
        'departments': departments,
        'selected_department': dept_id,
    }
    return render(request, 'services.html', context)


def get_doctors_by_department(request, dept_id):
    """AJAX endpoint to get doctors by department"""
    doctors = Doctor.objects.filter(specialization_id=dept_id, is_available=True)
    data = {
        'doctors': [{'id': d.id, 'name': f"Dr. {d.name}"} for d in doctors]
    }
    return JsonResponse(data)


def get_available_slots(request):
    """AJAX endpoint to get available appointment slots"""
    doctor_id = request.GET.get('doctor')
    appointment_date = request.GET.get('date')
    
    # Get existing appointments for this doctor on this date
    existing = Appointment.objects.filter(
        doctor_id=doctor_id,
        appointment_date=appointment_date,
        status='scheduled'
    ).values_list('appointment_time', flat=True)
    
    # Available times (9 AM to 5 PM with 30 min slots)
    all_times = _get_available_booking_times()
    available_times = [t for t in all_times if t not in existing]
    
    return JsonResponse({'available_times': available_times})


# Helper functions
def _get_available_booking_dates():
    """Get available dates for appointment booking (next 30 days, excluding Sundays)"""
    available_dates = []
    current_date = datetime.now().date() + timedelta(days=1)
    
    for i in range(30):
        check_date = current_date + timedelta(days=i)
        if check_date.weekday() != 6:  # Exclude Sundays (6)
            available_dates.append(check_date)
    
    return available_dates


def _get_available_booking_times():
    """Get available appointment times (30-minute slots from 9 AM to 5 PM)"""
    times = []
    start_hour = 9
    end_hour = 17
    
    for hour in range(start_hour, end_hour):
        for minute in [0, 30]:
            time_str = f"{hour:02d}:{minute:02d}"
            times.append(time_str)
    
    return times


# Cost Estimate
def cost_estimate(request):
    """Get cost estimate for a service"""
    if request.method == 'POST':
        service_id = request.POST.get('service')
        service = get_object_or_404(Service, id=service_id)
        
        return render(request, 'cost_estimate.html', {
            'service': service,
            'estimate': service.cost_estimate,
        })
    
    services = Service.objects.filter(cost_estimate__isnull=False)
    return render(request, 'cost_estimate_form.html', {'services': services})


# Authentication: registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto-login the user after registration
            login(request, user)
            return redirect('hospital_system:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


# Patient Dashboard (Profile)
@login_required(login_url='hospital_system:landing')
def patient_dashboard(request):
    """Patient dashboard showing appointments and profile"""
    try:
        patient = request.user.patient
    except Patient.DoesNotExist:
        # Handle case where user doesn't have a patient profile (shouldn't happen with new registration)
        return redirect('hospital_system:home')
    
    # Get user's appointments
    appointments = Appointment.objects.filter(
        patient_email=patient.email
    ).order_by('-appointment_date')
    
    context = {
        'patient': patient,
        'appointments': appointments,
    }
    return render(request, 'patient_dashboard.html', context)


# Update Patient Profile
@login_required(login_url='hospital_system:landing')
def update_profile(request):
    """Update patient profile"""
    try:
        patient = request.user.patient
    except Patient.DoesNotExist:
        return redirect('hospital_system:home')
    
    if request.method == 'POST':
        patient.phone = request.POST.get('phone', patient.phone)
        patient.date_of_birth = request.POST.get('date_of_birth', patient.date_of_birth)
        patient.gender = request.POST.get('gender', patient.gender)
        patient.blood_group = request.POST.get('blood_group', patient.blood_group)
        patient.address = request.POST.get('address', patient.address)
        patient.emergency_contact = request.POST.get('emergency_contact', patient.emergency_contact)
        patient.emergency_phone = request.POST.get('emergency_phone', patient.emergency_phone)
        patient.save()
        
        return redirect('hospital_system:patient_dashboard')
    
    context = {'patient': patient}
    return render(request, 'update_profile.html', context)
