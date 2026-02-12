from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import (
    Hospital, Department, Doctor, Patient, Appointment,
    Service, Infrastructure, Testimonial
)


# Inline admin for Patient linked to User
class PatientInline(admin.StackedInline):
    model = Patient
    fields = ('phone', 'date_of_birth', 'gender', 'blood_group', 'address', 'medical_history', 'emergency_contact', 'emergency_phone')
    extra = 0


# Extend the User admin to include Patient information
class UserAdmin(BaseUserAdmin):
    inlines = (PatientInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'phone', 'email')
    search_fields = ('name', 'location')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_doctor', 'created_at', 'get_image_preview')
    search_fields = ('name',)
    list_filter = ('created_at',)
    fields = ('name', 'description', 'icon', 'image', 'head_doctor')
    readonly_fields = ('get_image_preview',)
    
    def get_image_preview(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;" />', obj.image.url)
        return 'No image'
    get_image_preview.short_description = 'Image Preview'


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience_years', 'consultation_fee', 'is_available', 'get_image_preview')
    search_fields = ('name', 'qualification')
    list_filter = ('specialization', 'is_available', 'gender')
    readonly_fields = ('name', 'email', 'phone', 'get_image_preview')
    fields = ('name', 'email', 'phone', 'qualification', 'specialization', 'experience_years', 
              'consultation_fee', 'gender', 'availability', 'bio', 'image', 'get_image_preview', 'is_available')
    
    def get_image_preview(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html('<img src="{}" width="100" height="100" style="border-radius: 5px;" />', obj.image.url)
        return 'No image'
    get_image_preview.short_description = 'Image Preview'


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
