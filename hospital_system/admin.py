from django.contrib import admin
from .models import (
    Hospital, Department, Doctor, Patient, Appointment,
    Service, Infrastructure, Testimonial
)


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'phone', 'email')
    search_fields = ('name', 'location')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_doctor', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience_years', 'consultation_fee', 'is_available')
    search_fields = ('name', 'qualification')
    list_filter = ('specialization', 'is_available', 'gender')
    readonly_fields = ('name', 'email', 'phone')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'blood_group', 'registered_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('blood_group', 'gender', 'registered_at')
    readonly_fields = ('registered_at',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'doctor', 'appointment_date', 'appointment_time', 'status')
    search_fields = ('patient_name', 'patient_email', 'doctor__name')
    list_filter = ('status', 'appointment_date', 'department')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Patient Information', {
            'fields': ('patient_name', 'patient_email', 'patient_phone')
        }),
        ('Appointment Details', {
            'fields': ('doctor', 'department', 'appointment_date', 'appointment_time', 'reason')
        }),
        ('Status', {
            'fields': ('status', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'cost_estimate')
    search_fields = ('name',)
    list_filter = ('department',)


@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'hospital')
    search_fields = ('name',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'rating', 'doctor', 'is_published', 'created_at')
    search_fields = ('patient_name', 'patient_message')
    list_filter = ('rating', 'is_published', 'created_at')
    readonly_fields = ('created_at',)
