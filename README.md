# Arogya Medical Center - Hospital Management System

A comprehensive Django-based medical tech project with a professional frontend inspired by Apollo Hospitals. This system includes hospital management, doctor profiles, appointment booking, and patient management features.

## Features

### Core Features
- **Hospital Management**: Create and manage hospital information, departments, and infrastructure
- **Doctor Management**: Add doctors with specializations, qualifications, and consultation fees
- **Department Management**: Organize departments with descriptions and head doctors
- **Appointment Booking**: Full-featured online appointment booking system
- **Patient Management**: Store and manage patient information and medical history
- **Services/Treatments**: List and manage services with cost estimates
- **Testimonials**: Patient reviews and ratings system

### Frontend Features
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Apollo Hospitals Inspired**: Professional medical facility design
- **Dynamic Content**: Real-time doctor filtering by department
- **Appointment Slots**: Smart slot management with availability checking
- **Cost Estimates**: Transparent pricing information
- **Multi-page Navigation**: Complete site with home, departments, doctors, services, about, and contact pages

### Backend Features
- **Django Admin Panel**: Full admin interface for managing all content
- **Database Models**: Comprehensive models for all entities
- **AJAX Endpoints**: Dynamic data loading without page refresh
- **Form Validation**: Client-side and server-side validation

## Project Structure

```
project/
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
├── db.sqlite3                         # SQLite database (auto-created)
│
├── hospital_management/               # Main project configuration
│   ├── __init__.py
│   ├── settings.py                    # Project settings
│   ├── urls.py                        # Main URL configuration
│   └── wsgi.py                        # WSGI configuration
│
├── hospital_system/                   # Main Django app
│   ├── __init__.py
│   ├── models.py                      # Database models
│   ├── views.py                       # View functions
│   ├── urls.py                        # App URL routing
│   ├── admin.py                       # Admin configuration
│   └── apps.py                        # App configuration
│
├── templates/                         # HTML templates
│   ├── base.html                      # Base template
│   ├── index.html                     # Home page
│   ├── departments.html               # Departments listing
│   ├── department_detail.html         # Department details
│   ├── doctors.html                   # Doctors directory
│   ├── doctor_detail.html             # Doctor profile
│   ├── book_appointment.html          # Booking form
│   ├── appointment_confirmation.html  # Confirmation page
│   ├── services.html                  # Services listing
│   ├── about.html                     # About page
│   ├── contact.html                   # Contact page
│   ├── cost_estimate_form.html        # Cost estimate form
│   ├── cost_estimate.html             # Cost estimate display
│   └── contact_success.html           # Success messages
│
└── static/                            # Static files
    ├── css/
    │   └── style.css                  # Main stylesheet
    └── js/
        └── script.js                  # JavaScript utilities
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Configure Database

Run migrations to create the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Admin User

Create a superuser account for the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter username, email, and password.

### Step 4: Load Initial Data (Optional)

To populate the database with sample data, you can use Django's shell:

```bash
python manage.py shell
```

Then run these commands to create initial data:

```python
from hospital_system.models import Hospital, Department, Doctor, Service, Infrastructure

# Create Hospital
hospital = Hospital.objects.create(
    name="Arogya Medical Center",
    location="Ahmedabad, Gujarat",
    phone="9876543210",
    email="info@apollomedical.com",
    about="Leading medical facility providing comprehensive healthcare services.",
    established_year=2020,
    total_beds=500,
    doctors_count=200
)

# Create Departments
cardiology = Department.objects.create(
    name="Cardiology",
    description="Expert heart and cardiovascular care",
    icon="heart",
    head_doctor="Dr. Rajesh Kumar"
)

oncology = Department.objects.create(
    name="Oncology",
    description="Advanced cancer treatment and care",
    icon="disease",
    head_doctor="Dr. Priya Sharma"
)

orthopedics = Department.objects.create(
    name="Orthopedics",
    description="Bone, joint, and ligament specialist care",
    icon="bone",
    head_doctor="Dr. Ahmad Hassan"
)

# Create Doctors
doctor1 = Doctor.objects.create(
    name="Rajesh Kumar",
    email="rajesh@hospital.com",
    phone="9876543210",
    qualification="MD (Cardiology), FACC",
    specialization=cardiology,
    experience_years=15,
    consultation_fee=500,
    gender="M",
    availability="Monday to Saturday, 10 AM - 4 PM",
    bio="Highly experienced cardiologist with expertise in interventional cardiology."
)

doctor2 = Doctor.objects.create(
    name="Priya Sharma",
    email="priya@hospital.com",
    phone="9876543211",
    qualification="MD (Oncology), DNB",
    specialization=oncology,
    experience_years=12,
    consultation_fee=600,
    gender="F",
    availability="Monday to Friday, 11 AM - 5 PM",
    bio="Specialized in various cancer treatments and chemotherapy."
)

# Create Services
Service.objects.create(
    name="Angiography",
    description="Diagnostic heart imaging procedure",
    department=cardiology,
    cost_estimate=15000
)

Service.objects.create(
    name="Chemotherapy",
    description="Advanced cancer treatment",
    department=oncology,
    cost_estimate=50000
)

# Create Infrastructure
Infrastructure.objects.create(
    name="MRI Machine",
    description="Advanced magnetic resonance imaging equipment",
    icon="brain",
    hospital=hospital
)

Infrastructure.objects.create(
    name="Operation Theatre",
    description="State-of-the-art operating rooms with latest technology",
    icon="hospital",
    hospital=hospital
)
```

Type `exit()` to exit the shell.

### Step 5: Run Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be available at:
- **Main Site**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Usage

### Accessing the Application

**Home Page**: http://127.0.0.1:8000/
- View hospital information, departments, and infrastructure
- See patient testimonials

**Departments**: http://127.0.0.1:8000/departments/
- Browse all medical departments
- Click to view department details, services, and specialists

**Doctors**: http://127.0.0.1:8000/doctors/
- Search doctors by name or specialization
- Filter by department
- View detailed doctor profiles

**Book Appointment**: http://127.0.0.1:8000/book-appointment/
- Fill appointment form with patient details
- Select doctor, date, and time slot
- Submit for confirmation

**Services**: http://127.0.0.1:8000/services/
- Browse medical services and treatments
- View cost estimates
- Filter by department

**Admin Panel**: http://127.0.0.1:8000/admin/
- Manage all hospital data
- Add/edit doctors, departments, appointments
- View patient information
- Manage testimonials

## Database Models

### Hospital
- Name, Location, Contact Info
- About, Established Year
- Total Beds, Doctors Count

### Department
- Name, Description
- Icon (Font Awesome)
- Head Doctor Name
- Timestamps

### Doctor
- Personal Info: Name, Email, Phone
- Professional: Qualification, Specialization, Experience
- Consultation Fee, Gender
- Availability, Bio, Image
- Availability Status

### Patient
- Personal Info: Name, Email, Phone, DOB
- Medical Info: Blood Group, Medical History
- Emergency Contact Details
- Registration Timestamp

### Appointment
- Patient Details
- Doctor & Department
- Date & Time
- Reason for Visit
- Status (Scheduled, Completed, Cancelled, No-Show)
- Notes & Timestamps

### Service
- Name, Description
- Department Link
- Cost Estimate

### Infrastructure
- Name, Description
- Icon, Hospital Link

### Testimonial
- Patient Name & Message
- Rating (1-5)
- Doctor Reference
- Published Status
- Timestamps

## API Endpoints

### AJAX Endpoints
- `GET /api/doctors-by-department/<dept_id>/` - Get doctors for a department
- `GET /api/available-slots/?doctor=<id>&date=<date>` - Get available appointment slots

## Customization

### Add Hospital Information
Edit `hospital_management/settings.py` to customize:
- Hospital name
- Logo/branding
- Default timezone
- Email settings

### Modify Styling
Edit `static/css/style.css` to customize:
- Colors (primary, secondary, accent)
- Fonts and spacing
- Responsive breakpoints
- Component styles

### Add More Features
Extend the project by:
- Adding online payment integration
- Implementing email notifications
- Adding PDF report generation
- Creating mobile app with React Native

## Email Configuration

To enable email notifications, add to `hospital_management/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

## Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Update `ALLOWED_HOSTS` with your domain
3. Use a production database (PostgreSQL recommended)
4. Configure static files collection
5. Set up proper HTTPS/SSL
6. Use GunicornWSGI server
7. Set up Nginx or Apache as reverse proxy

## Troubleshooting

### Port Already in Use
If port 8000 is already in use:
```bash
python manage.py runserver 8080
```

### Database Issues
Reset the database:
```bash
python manage.py flush
python manage.py migrate
```

### Missing Static Files
Collect static files:
```bash
python manage.py collectstatic --noinput
```

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Future Enhancements

- [ ] Online payment integration
- [ ] SMS/Email notifications
- [ ] Video consultation feature
- [ ] Medical records management
- [ ] Lab test integration
- [ ] Prescription management
- [ ] Insurance claim processing
- [ ] Multi-language support
- [ ] Mobile app (iOS/Android)
- [ ] Real-time chat support

## Credits

Designed with inspiration from Apollo Hospitals website for a professional medical facility interface.

## Support

For issues or questions:
- Check the troubleshooting section
- Review Django documentation: https://docs.djangoproject.com/
- Check browser console for errors (F12)

## License

This project is provided as-is for educational and development purposes.

---

**Last Updated**: February 8, 2026
**Version**: 1.0.0
