import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

user, created = User.objects.get_or_create(username='Geologyrenni')
user.set_password('otanerstudio')
user.is_superuser = True
user.is_staff = True
user.is_active = True
user.save()

print("Përdoruesi u përditësua me sukses!")