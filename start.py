import os
from django.core.management import execute_from_command_line

username = os.getenv('DJANGO_SUPERUSER_USERNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if username and email and password:
    try:
        execute_from_command_line(['manage.py', 'createsuperuser', '--noinput'])
        print("Superuser created successfully.")
    except Exception as e:
        print(f"Superuser creation failed: {e}")