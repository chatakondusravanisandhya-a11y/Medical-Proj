from django.core.management.base import BaseCommand
from hospital_system.models import Hospital, Department, Doctor, Service, Infrastructure, Testimonial


class Command(BaseCommand):
    help = 'Seed database with sample hospital, departments, doctors, services and infra'

    def handle(self, *args, **options):
        # Create Hospital
        hospital, _ = Hospital.objects.get_or_create(
            name='Arogya Medical Center',
            defaults={
                'location': 'Ahmedabad, Gujarat',
                'phone': '9876543210',
                'email': 'info@apollomedical.com',
                'website': 'https://www.apollohospitals.com',
                'about': 'Leading medical facility providing comprehensive healthcare services.',
                'established_year': 2000,
                'total_beds': 350,
                'doctors_count': 120,
            }
        )

        # Ten departments
        dept_names = [
            ('Cardiology', 'Heart and vascular care'),
            ('Oncology', 'Cancer care and treatments'),
            ('Orthopedics', 'Bone and joint specialists'),
            ('Gastroenterology', 'Digestive system specialists'),
            ('Neurology', 'Brain and nervous system care'),
            ('Urology', 'Urinary and reproductive health'),
            ('Nephrology', 'Kidney care and dialysis'),
            ('Pulmonology', 'Lung and respiratory care'),
            ('Gynecology', 'Women health and maternity'),
            ('Pediatrics', 'Child health and neonatology'),
        ]

        depts = []
        for name, desc in dept_names:
            d, _ = Department.objects.get_or_create(name=name, defaults={'description': desc, 'icon': 'user-md'})
            depts.append(d)

        # Create sample doctors (one or two per department)
        sample_doctors = []
        for i, d in enumerate(depts, start=1):
            doc_name = f"Dr. {d.name.split()[0]} Expert"
            doc_email = f"{d.name.lower()}@apollomedical.com".replace(' ', '')
            doc_phone = f"90000000{i:02d}"
            doctor, created = Doctor.objects.get_or_create(
                name=doc_name,
                defaults={
                    'email': doc_email,
                    'phone': doc_phone,
                    'qualification': 'MBBS, MD',
                    'specialization': d,
                    'experience_years': 10 + i,
                    'consultation_fee': 500 + i * 50,
                    'gender': 'M' if i % 2 == 0 else 'F',
                    'availability': 'Mon-Fri, 10:00-16:00',
                    'bio': f'Experienced specialist in {d.name}.',
                    'is_available': True,
                }
            )
            sample_doctors.append(doctor)

        # Add services
        services_list = [
            ('Angiography', 'Heart imaging procedure', depts[0], 15000),
            ('Chemotherapy', 'Cancer treatment', depts[1], 45000),
            ('Joint Replacement', 'Orthopedic joint replacement', depts[2], 80000),
            ('Endoscopy', 'GI diagnostic procedure', depts[3], 8000),
            ('EEG', 'Neurological diagnostic test', depts[4], 5000),
        ]
        for name, desc, dept, cost in services_list:
            Service.objects.get_or_create(name=name, department=dept, defaults={'description': desc, 'cost_estimate': cost})

        # Infrastructure
        infra_items = [
            ('MRI Machine', 'High-resolution MRI', 'brain'),
            ('Robotic Surgery Suite', 'Robotic-assisted surgery', 'robot'),
            ('Cath Lab', 'Cardiac catheterization lab', 'heart'),
        ]
        for name, desc, icon in infra_items:
            Infrastructure.objects.get_or_create(name=name, hospital=hospital, defaults={'description': desc, 'icon': icon})

        # Testimonials
        Testimonial.objects.get_or_create(patient_name='Ravi Patel', defaults={'patient_message': 'Excellent care and friendly staff.', 'rating': 5, 'is_published': True})
        Testimonial.objects.get_or_create(patient_name='Sneha Rao', defaults={'patient_message': 'Very experienced doctors and smooth process.', 'rating': 4, 'is_published': True})

        self.stdout.write(self.style.SUCCESS('Sample data seeded successfully.'))
