import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','hospital_management.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = 'admin'
password = 'AdminPass123'
email = 'admin@example.com'

user = User.objects.filter(username=username).first()
if user:
    print('SUPERUSER_EXISTS')
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print('SUPERUSER_CREATED')
