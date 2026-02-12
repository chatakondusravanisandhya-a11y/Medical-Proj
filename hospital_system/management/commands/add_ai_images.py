"""
Management command to add AI-generated pictures for doctors and departments.
Uses placeholder image services and provides instructions for integration with AI services.
"""
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
from io import BytesIO
from hospital_system.models import Doctor, Department


class Command(BaseCommand):
    help = 'Add AI-generated or placeholder pictures for doctors and departments'

    def add_arguments(self, parser):
        parser.add_argument(
            '--type',
            type=str,
            choices=['doctors', 'departments', 'both'],
            default='both',
            help='Type of images to generate: doctors, departments, or both'
        )
        parser.add_argument(
            '--service',
            type=str,
            choices=['placeholder', 'unsplash', 'pexels'],
            default='placeholder',
            help='Image service to use'
        )

    def handle(self, *args, **options):
        image_type = options['type']
        service = options['service']

        if image_type in ['doctors', 'both']:
            self.add_doctor_images(service)

        if image_type in ['departments', 'both']:
            self.add_department_images(service)

        self.stdout.write(self.style.SUCCESS('✓ Image addition process completed!'))
        self.stdout.write(self.style.WARNING(
            'Note: To use AI-generated pictures, integrate with services like:\n'
            '- OpenAI DALL-E API\n'
            '- Stability AI API\n'
            '- Hugging Face API\n'
            'Upload images through Django admin panel with your preferred service.'
        ))

    def get_placeholder_url(self, name, category='avatar'):
        """Generate a placeholder image URL"""
        if category == 'doctor':
            # Using UI Avatars service for doctor images
            return f"https://ui-avatars.com/api/?name={name.replace(' ', '+')}&size=400&background=667eea&color=fff&bold=true"
        elif category == 'department':
            # Using placeholder service for department images
            return f"https://via.placeholder.com/800x600/667eea/ffffff?text={name.replace(' ', '+')}"
        return None

    def get_unsplash_url(self, query, width=400, height=400):
        """Get image from Unsplash"""
        try:
            url = f"https://source.unsplash.com/{width}x{height}/?{query}"
            return url
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error fetching from Unsplash: {e}'))
            return None

    def add_doctor_images(self, service):
        """Add images for doctors without images"""
        doctors_without_images = Doctor.objects.filter(image='')

        if not doctors_without_images.exists():
            self.stdout.write(self.style.SUCCESS('All doctors already have images!'))
            return

        self.stdout.write(f'Found {doctors_without_images.count()} doctors without images.')

        for doctor in doctors_without_images:
            try:
                if service == 'placeholder':
                    image_url = self.get_placeholder_url(doctor.name, 'doctor')
                elif service == 'unsplash':
                    image_url = self.get_unsplash_url(f'doctor,{doctor.specialization.name.lower()}', 400, 400)
                else:
                    image_url = None

                if image_url:
                    # Download and save the image
                    response = requests.get(image_url, timeout=10)
                    if response.status_code == 200:
                        filename = f'doctor_{doctor.id}.jpg'
                        doctor.image.save(filename, ContentFile(response.content), save=True)
                        self.stdout.write(
                            self.style.SUCCESS(f'✓ Added image for Dr. {doctor.name}')
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'⚠ Failed to download image for Dr. {doctor.name}')
                        )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Error processing Dr. {doctor.name}: {e}'))

    def add_department_images(self, service):
        """Add images for departments without images"""
        depts_without_images = Department.objects.filter(image='')

        if not depts_without_images.exists():
            self.stdout.write(self.style.SUCCESS('All departments already have images!'))
            return

        self.stdout.write(f'Found {depts_without_images.count()} departments without images.')

        for dept in depts_without_images:
            try:
                if service == 'placeholder':
                    image_url = self.get_placeholder_url(dept.name, 'department')
                elif service == 'unsplash':
                    image_url = self.get_unsplash_url(f'{dept.name.lower()},medical', 800, 600)
                else:
                    image_url = None

                if image_url:
                    # Download and save the image
                    response = requests.get(image_url, timeout=10)
                    if response.status_code == 200:
                        filename = f'dept_{dept.id}.jpg'
                        dept.image.save(filename, ContentFile(response.content), save=True)
                        self.stdout.write(
                            self.style.SUCCESS(f'✓ Added image for {dept.name}')
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(f'⚠ Failed to download image for {dept.name}')
                        )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Error processing {dept.name}: {e}'))
