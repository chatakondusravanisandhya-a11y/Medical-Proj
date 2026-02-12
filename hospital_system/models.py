from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Hospital Model
class Hospital(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit phone number')]
    )
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    about = models.TextField()
    established_year = models.IntegerField()
    total_beds = models.IntegerField()
    doctors_count = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Hospitals"


# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='stethoscope', help_text='Font Awesome icon name')
    image = models.ImageField(upload_to='departments/', blank=True, null=True, help_text='Department image or AI-generated picture')
    head_doctor = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Departments"


# Doctor Model
class Doctor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=200)
    specialization = models.ForeignKey(Department, on_delete=models.CASCADE)
    experience_years = models.IntegerField()
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    availability = models.CharField(max_length=100, default='Monday to Saturday')
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Dr. {self.name}"
    
    class Meta:
        ordering = ['name']


# Service/Treatment Model
class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    cost_estimate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return self.name


# Patient Model
class Patient(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient', null=True, blank=True)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True)
    address = models.TextField(blank=True)
    medical_history = models.TextField(blank=True)
    emergency_contact = models.CharField(max_length=150, blank=True)
    emergency_phone = models.CharField(max_length=15, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-registered_at']


# Appointment Model
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no-show', 'No Show'),
    ]
    
    patient_name = models.CharField(max_length=150)
    patient_email = models.EmailField()
    patient_phone = models.CharField(max_length=15)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name} ({self.appointment_date})"
    
    class Meta:
        ordering = ['-appointment_date']
        unique_together = ['doctor', 'appointment_date', 'appointment_time']


# Hospital Infrastructure Model
class Infrastructure(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='hospital', help_text='Font Awesome icon name')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Infrastructure"


# Testimonial Model
class Testimonial(models.Model):
    patient_name = models.CharField(max_length=150)
    patient_message = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Review by {self.patient_name}"
    
    class Meta:
        ordering = ['-created_at']
